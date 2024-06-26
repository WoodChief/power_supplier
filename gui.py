
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QRectF, Qt
import argparse
from widgets import TempGraphWidget
from os import listdir
import os
import json
from munch import Munch
import can
import can.interfaces.gs_usb
import threading
import usb
import time

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', default='windows')
args = parser.parse_args()

if args.platform == 'windows':
    from mainwindow import Ui_mainWindow
elif args.platform == 'portable':
    from portwindow import Ui_mainWindow

# CAN bus init #
with open('CAN.json') as f:
    json_dict = json.load(f)
    can_settings = Munch.fromDict(json_dict)[os.name]

can_connection_event = threading.Event()
can_connection_event.clear()
try:
    if os.name == 'posix':
        password = 'woodman'
        os.system(f"echo {password} "
                  f"| sudo -S ip link set {can_settings.channel} up "
                  f"type can bitrate {can_settings.bitrate}")
        bus = can.Bus(interface=can_settings.interface,
                      channel=can_settings.channel,
                      bitrate=can_settings.bitrate)
        can_connection_event.set()
    elif os.name == 'nt':
        dev = usb.core.find(idVendor=0x1d50, idProduct=0x606f)
        bus = can.interfaces.gs_usb.GsUsbBus(
            channel=dev.product,
            bus=dev.bus,
            address=dev.address,
            bitrate=can_settings.bitrate
        )
        can_connection_event.set()
except (AttributeError, OSError):
    print("Please connect dedicated USB-CAN interface!")


mes = can.Message()
mes.is_extended_id = can_settings.extended_id
mes.dlc = can_settings.dlc

# Power supply presets init #
settings_path = 'settings/'
# Make power supply settings first in the settings list
power_settings_file = 'power_supply_settings.json'

settings_files = [power_settings_file]
settings_files = settings_files + [f for f in listdir(settings_path)
                                   if (f.endswith('json')
                                       and not f.startswith('power'))]
settings = []

# Add presets to the  settings list
for file in settings_files:
    with open(settings_path + file, encoding='utf-8') as f:
        json_dict = json.load(f)
        settings.append(Munch.fromDict(json_dict))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the ui file #
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("images/logoColor.ico"))

        self.temp_graph = TempGraphWidget(self.ui.tempGraphFrame, args.platform)
        self.temp_graph.setGeometry(-10, 15, 200, 100)
        self.temp_graph.chart.setPlotArea(QRectF(0, 0, 200, 100))
        self.temp_graph.lower()

        # Supporting variables
        self.prev_mes = can.Message()

        # Threads
        self.can_receive_thread = threading.Thread(target=self.can_receive)
        self.can_receive_thread.daemon = True
        self.can_receive_thread.start()

        # Hide widgets wich are not active
        self.ui.durationFrame.hide()
        self.ui.frequencyFrame.hide()
        self.ui.connectIconLabel.hide()

        # Default text labels
        self.ui.powerSupplyNumberLabel.setText('Нет соединения')

        # Fill presetComboBox
        self.ui.presetComboBox.clear()

        # Current power supply settings item
        # for dev in settings:
        #     self.ui.presetComboBox.addItem(dev.name)
        # temporarily excluded laser presets
        self.ui.presetComboBox.addItem(settings[0].name)

        # Load power supply settings
        self.load_device(0)

        # Get power supply capabilities and correct settings
        self.get_saved_settings()

        # Connection between widget (not accessable from designer)
        self.ui.currentValueDoubleSpinBox.valueChanged.connect(
            self.on_current_spinbox_value_changed
        )
        self.ui.currentSlider.valueChanged.connect(
            self.on_current_slider_value_change
        )
        self.ui.rangeTempMinSpinBox.valueChanged.connect(
            self.ui.rangeTempMaxSpinBox.setMinimum
        )
        self.ui.rangeTempMaxSpinBox.valueChanged.connect(
            self.ui.rangeTempMinSpinBox.setMaximum
        )
        self.ui.currentMinusFivePushButton.pressed.connect(
            lambda: self.on_current_button_pressed(-5)
        )
        self.ui.currentMinusOnePushButton.pressed.connect(
            lambda: self.on_current_button_pressed(-1)
        )
        self.ui.currentPlusOnePushButton.pressed.connect(
            lambda: self.on_current_button_pressed(1)
        )
        self.ui.currentPlusFivePushButton.pressed.connect(
            lambda: self.on_current_button_pressed(5)
        )
        self.ui.durationMinusTwentyPushButton.pressed.connect(
            lambda: self.on_duration_button_pressed(-20)
        )
        self.ui.durationMinusTenPushButton.pressed.connect(
            lambda: self.on_duration_button_pressed(-10)
        )
        self.ui.durationPlusTenPushButton.pressed.connect(
            lambda: self.on_duration_button_pressed(10)
        )
        self.ui.durationPlusTwentyPushButton.pressed.connect(
            lambda: self.on_duration_button_pressed(20)
        )
        self.ui.frequencyMinusFivePushButton.pressed.connect(
            lambda: self.on_frequency_button_pressed(-5)
        )
        self.ui.frequencyMinusOnePushButton.pressed.connect(
            lambda: self.on_frequency_button_pressed(-1)
        )
        self.ui.frequencyPlusOnePushButton.pressed.connect(
            lambda: self.on_frequency_button_pressed(1)
        )
        self.ui.frequencyPlusFivePushButton.pressed.connect(
            lambda: self.on_frequency_button_pressed(5)
        )

        # Connections #
        self.ui.presetComboBox.currentIndexChanged.connect(
            lambda: self.load_device(self.ui.presetComboBox.currentIndex())
        )
        self.ui.presetPushButton.pressed.connect(
            self.on_preset_push_button_pressed
        )
        self.ui.sendPushButton.pressed.connect(
            self.on_send_push_button_pressed
        )
        self.ui.savePushButton.pressed.connect(
            self.on_save_push_button_pressed
        )
        self.ui.stopRadioButton.clicked.connect(
            self.on_start_stop_button_pressed
        )
        self.ui.startRadioButton.clicked.connect(
            self.on_start_stop_button_pressed
        )
        self.ui.externalTriggerRadioButton.clicked.connect(
            self.on_start_stop_button_pressed
        )
        self.ui.PCDCheckBox.clicked.connect(
            self.on_checkbox_state_changed
        )
        self.ui.jitterStabCheckBox.clicked.connect(
            self.on_checkbox_state_changed
        )
        self.ui.offFDPumpingCheckBox.clicked.connect(
            self.on_checkbox_state_changed
        )
        self.ui.rangefinderCheckBox.clicked.connect(
            self.on_checkbox_state_changed
        )
        self.ui.offTempRadioButton.clicked.connect(
            self.on_tec_mode_changed
        )
        self.ui.stabTempRadioButton.clicked.connect(
            self.on_tec_mode_changed
        )
        self.ui.rangeTempRadioButton.clicked.connect(
            self.on_tec_mode_changed
        )
        self.ui.durationValueSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.durationValueSpinBox)
        )
        self.ui.frequencyValueSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.frequencyValueSpinBox)
        )
        self.ui.voltageValueDoubleSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.voltageValueDoubleSpinBox)
        )
        self.ui.delayValueSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.voltageValueDoubleSpinBox)
        )
        self.ui.delayValueSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.delayValueSpinBox)
        )
        self.ui.PWMValueSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.PWMValueSpinBox)
        )
        self.ui.stabTempDoubleSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.stabTempDoubleSpinBox)
        )
        self.ui.rangeTempMinSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.rangeTempMinSpinBox)
        )
        self.ui.rangeTempMaxSpinBox.valueChanged.connect(
            lambda: self.set_highlighting(self.ui.rangeTempMaxSpinBox)
        )
        self.ui.tempGraphPlusPushButton.pressed.connect(
            self.on_temp_plus_push_button_pressed
        )
        self.ui.tempGraphMinusPushButton.pressed.connect(
            self.on_temp_minus_push_button_pressed
        )

    def on_frequency_button_pressed(self, increment):
        self.ui.frequencyValueSpinBox.setValue(
            self.ui.frequencyValueSpinBox.value() + increment
        )
        self.ui.frequencyValueSpinBox.setStyleSheet("u")
        self.prepare_settings_values()
        self.send_812()

    def on_duration_button_pressed(self, increment):
        self.ui.durationValueSpinBox.setValue(
            self.ui.durationValueSpinBox.value() + increment
        )
        self.ui.durationValueSpinBox.setStyleSheet(u"")
        self.prepare_settings_values()
        self.send_813()

    def on_current_button_pressed(self, increment):
        self.ui.currentValueDoubleSpinBox.setValue(
            self.ui.currentValueDoubleSpinBox.value() + increment
        )
        self.ui.currentValueDoubleSpinBox.setStyleSheet(u"")
        self.prepare_settings_values()
        self.send_813()

    def on_current_spinbox_value_changed(self):
        self.ui.currentSlider.setValue(
            int(self.ui.currentValueDoubleSpinBox.value() * 10)
        )
        self.set_highlighting(self.ui.currentValueDoubleSpinBox)

    def on_current_slider_value_change(self):
        self.ui.currentValueDoubleSpinBox.setValue(
            self.ui.currentSlider.value() / 10
        )

    def load_device(self, index):
        self.device = settings[index]

        # CURRENT #
        self.ui.currentValueDoubleSpinBox.setValue(
            self.device.current.current
        )
        self.ui.currentValueDoubleSpinBox.setMinimum(
            self.device.current.min_current
        )
        self.ui.currentValueDoubleSpinBox.setMaximum(
            self.device.current.max_current
        )
        self.ui.currentSlider.setValue(
            self.device.current.current * 10
        )
        self.ui.currentSlider.setMinimum(
            self.device.current.min_current * 10
        )
        self.ui.currentSlider.setMaximum(
            self.device.current.max_current * 10
        )
        self.ui.currentMinLabel.setText(
            str(self.device.current.min_current)
        )
        self.ui.currentMaxLabel.setText(
            str(self.device.current.max_current)
        )

        # DURATION #
        self.ui.durationValueSpinBox.setValue(
            self.device.duration.duration
        )
        self.ui.durationValueSpinBox.setMinimum(
            self.device.duration.min_duration
        )
        self.ui.durationValueSpinBox.setMaximum(
            self.device.duration.max_duration
        )
        self.ui.durationSlider.setMinimum(
            self.device.duration.min_duration
        )
        self.ui.durationSlider.setMaximum(
            self.device.duration.max_duration
        )
        self.ui.durationMinLabel.setText(
            str(self.device.duration.min_duration)
        )
        self.ui.durationMaxLabel.setText(
            str(self.device.duration.max_duration)
        )

        # FREQUENCY #
        self.ui.frequencyValueSpinBox.setValue(
            self.device.frequency.frequency
        )
        self.ui.frequencyValueSpinBox.setMinimum(
            self.device.frequency.min_frequency
        )
        self.ui.frequencyValueSpinBox.setMaximum(
            self.device.frequency.max_frequency
        )
        self.ui.frequencySlider.setMinimum(
            self.device.frequency.min_frequency
        )
        self.ui.frequencySlider.setMaximum(
            self.device.frequency.max_frequency
        )
        self.ui.frequencyMinLabel.setText(
            str(self.device.frequency.min_frequency)
        )
        self.ui.frequencyMaxLabel.setText(
            str(self.device.frequency.max_frequency)
        )
        self.ui.factDurationValueLabel.setText('none')

        self.device.frequency.pulse_period_mks = (
            int(1 / self.ui.frequencyValueSpinBox.value() * 10**6)
        )

        # VOLTAGE #
        self.ui.voltageValueDoubleSpinBox.setValue(
            self.device.voltage.voltage
        )
        self.ui.voltageValueDoubleSpinBox.setMinimum(
            self.device.voltage.min_voltage
        )
        self.ui.voltageValueDoubleSpinBox.setMaximum(
            self.device.voltage.max_voltage
        )

        # QSWITCH #
        self.ui.delayValueSpinBox.setValue(
            self.device.qswitch.delay
        )
        self.ui.delayValueSpinBox.setMinimum(
            self.device.qswitch.min_delay
        )
        self.ui.delayValueSpinBox.setMaximum(
            self.device.qswitch.max_delay
        )
        self.ui.PWMValueSpinBox.setValue(
            self.device.qswitch.pwm
        )

        # RANGE FINDER #
        self.ui.rangefinderValueLabel.setText('0')
        self.ui.rangefinderCheckBox.setChecked(
            self.device.range_finder.mode
        )

        # TEC #
        self.ui.stabTempDoubleSpinBox.setValue(
            self.device.tec.stabilization_temp
        )
        self.ui.stabTempDoubleSpinBox.setMinimum(
            self.device.tec.min_stabilization_temp
        )
        self.ui.stabTempDoubleSpinBox.setMaximum(
            self.device.tec.max_stabilization_temp
        )
        self.ui.rangeTempMinSpinBox.setValue(
            self.device.tec.min_range_temp
        )
        self.ui.rangeTempMinSpinBox.setMinimum(
            self.device.tec.min_stabilization_temp
        )
        self.ui.rangeTempMinSpinBox.setMaximum(
            self.device.tec.max_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setValue(
            self.device.tec.max_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setMinimum(
            self.device.tec.min_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setMaximum(
            self.device.tec.max_stabilization_temp
        )
        self.ui.tempGraphValueLabel.setText(
            str(self.device.tec.current_temp)
        )

        if self.device.tec.tec_mode == 0:
            self.ui.offTempRadioButton.click()
        elif self.device.tec.tec_mode == 1:
            self.ui.stabTempRadioButton.click()
        elif self.device.tec.tec_mode == 2:
            self.ui.rangeTempRadioButton.click()

        # FEATURES #
        self.ui.PCDCheckBox.setChecked(
            self.device.features.pcd_21
        )
        self.ui.jitterStabCheckBox.setChecked(
            self.device.features.jitter_stabilizer
        )
        self.ui.offFDPumpingCheckBox.setChecked(
            self.device.features.stop_diode
        )

    def prepare_settings_values(self):
        self.device.current.current = self.ui.currentValueDoubleSpinBox.value()
        self.device.duration.duration = self.ui.durationValueSpinBox.value()
        self.device.frequency.frequency = self.ui.frequencyValueSpinBox.value()
        self.device.voltage.voltage = self.ui.voltageValueDoubleSpinBox.value()
        self.device.qswitch.delay = self.ui.delayValueSpinBox.value()
        self.device.qswitch.pwm = self.ui.PWMValueSpinBox.value()
        self.device.features.pcd_21 = self.ui.PCDCheckBox.isChecked()
        self.device.features.jitter_stabilizer = (
            self.ui.jitterStabCheckBox.isChecked()
            )
        self.device.features.stop_diode = (
            self.ui.offFDPumpingCheckBox.isChecked()
            )
        self.device.range_finder.mode = self.ui.rangefinderCheckBox.isChecked()
        if self.ui.offTempRadioButton.isChecked():
            self.device.tec.tec_mode = 0
        elif self.ui.stabTempRadioButton.isChecked():
            self.device.tec.tec_mode = 1
        elif self.ui.rangeTempRadioButton.isChecked():
            self.device.tec.tec_mode = 2
        self.device.tec.stabilization_temp = (
            self.ui.stabTempDoubleSpinBox.value()
            )
        self.device.tec.min_range_temp = self.ui.rangeTempMinSpinBox.value()
        self.device.tec.max_range_temp = self.ui.rangeTempMaxSpinBox.value()

    def on_preset_push_button_pressed(self):
        index = self.ui.presetComboBox.currentIndex()
        self.prepare_settings_values()
        print(settings[index], '\n')
        file = settings_path + settings_files[index]
        print('Path to save settings:', file)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(settings[index], f, ensure_ascii=False)

    def on_send_push_button_pressed(self):
        self.prepare_settings_values()
        self.send_813()
        self.send_814()
        self.send_815()
        self.send_816()
        self.send_817()
        self.send_818()
        self.send_812()
        self.reset_highlighting()

    def on_start_stop_button_pressed(self):
        self.prepare_settings_values()
        self.send_812()
        self.ui.currentValueDoubleSpinBox.setStyleSheet(u"")
        self.ui.durationValueSpinBox.setStyleSheet(u"")
        self.ui.frequencyValueSpinBox.setStyleSheet(u"")

    def on_checkbox_state_changed(self):
        self.prepare_settings_values()
        self.send_815()
        self.send_816()

    def on_tec_mode_changed(self):
        # self.prepare_settings_values()
        self.send_814()

    def on_temp_plus_push_button_pressed(self):
        self.temp_graph.zoom(1.25)

    def on_temp_minus_push_button_pressed(self):
        self.temp_graph.zoom(0.8)

    def send_can(self):
        if can_connection_event.is_set():
            bus.send(mes)
            time.sleep(0.01)
        else:
            self.ui.powerSupplyNumberLabel.setText(
                'Ошибка CAN'
            )
            self.ui.powerSupplyNumberLabel.setStyleSheet(
                u"QLabel {color: 'red'}")

    def send_812(self):
        mes.arbitration_id = 812
        if self.ui.stopRadioButton.isChecked():
            mode = 0
        elif self.ui.startRadioButton.isChecked():
            mode = 1
        # mode = 2 is not implemented yet
        elif self.ui.externalTriggerRadioButton.isChecked():
            mode = 3
        pulse_period_mks = int(1 / self.ui.frequencyValueSpinBox
                               .value() * 10**6)
        mes.data = list(
            mode.to_bytes(1, 'big')
            + b'\x00\x00'  # unlimited number of pulses
            + pulse_period_mks.to_bytes(3, 'big')
            # + b'\x00'  # should be a sequence number
        )
        self.send_can()

    def send_813(self):
        mes.arbitration_id = 813
        mes.data = list(
            int(self.ui.currentValueDoubleSpinBox.value() * 10)
            .to_bytes(2, 'big')
            + self.ui.durationValueSpinBox.value().to_bytes(2, 'big')
            + int(self.ui.voltageValueDoubleSpinBox.value() * 10)
            .to_bytes(2, 'big')
            # + safe_mode  # not implemented yet
        )
        self.send_can()

    def send_814(self):
        mes.arbitration_id = 814
        if self.ui.offTempRadioButton.isChecked():
            tec_mode = 0
        elif self.ui.stabTempRadioButton.isChecked():
            tec_mode = 1
        elif self.ui.rangeTempRadioButton.isChecked():
            tec_mode = 2
        mes.data = list(
            tec_mode.to_bytes(1, 'big')
            + int(self.ui.stabTempDoubleSpinBox.value() * 10)
            .to_bytes(2, 'big')
            + self.ui.rangeTempMaxSpinBox.value().to_bytes(1, 'big')
            + self.ui.rangeTempMinSpinBox.value().to_bytes(1, 'big')
        )
        self.send_can()

    def send_815(self):
        mes.arbitration_id = 815
        mes.data = list(
            self.ui.PCDCheckBox.isChecked().to_bytes(1, 'big')
            + self.ui.PWMValueSpinBox.value().to_bytes(1, 'big')
            + self.ui.delayValueSpinBox.value().to_bytes(1, 'big', signed=True)
            + self.ui.rangefinderCheckBox.isChecked().to_bytes(1, 'big')
        )
        self.send_can()

    def send_816(self):
        mes.arbitration_id = 816
        mes.data = list(
            self.ui.jitterStabCheckBox.isChecked().to_bytes(1, 'big')
            + self.ui.offFDPumpingCheckBox.isChecked().to_bytes(1, 'big')
            # + current_addition
            # + current_addition_value
            # + current_addition_time
        )
        self.send_can()

    def send_817(self):
        mes.arbitration_id = 817
        # PID settings # not implemented yet
        pass

    def send_818(self):
        pass

    def on_save_push_button_pressed(self):
        mes.arbitration_id = 811
        mes.data = list((4).to_bytes(1, 'big'))
        self.send_can()

    def get_saved_settings(self):
        mes.arbitration_id = 811
        mes.data = list((1).to_bytes(1, 'big'))
        self.send_can()

    def can_parser(self):
        response = bus.recv(0.02)
        if (response is not None) and (
                response.timestamp != self.prev_mes.timestamp):
            self.prev_mes = response
            data = bytes(response.data)
            if response.arbitration_id == 830:
                pass
            elif response.arbitration_id == 831:
                pass
            elif response.arbitration_id == 832:
                self.ui.powerSupplyNumberLabel.setText(
                    f"Блок питания №{int.from_bytes(data[:2], 'big')}"
                )
                self.ui.disconnectIconLabel.hide()
                self.ui.connectIconLabel.show()
                state = data[2]
                if state == 0:
                    self.ui.stopRadioButton.setChecked(True)
                elif state == 1:
                    self.ui.startRadioButton.setChecked(True)
                elif state == 2:
                    # not implemented yet
                    pass
                elif state == 3:
                    self.ui.externalTriggerRadioButton.setChecked(True)
                elif state == 4:
                    # Here should be adn ERROR handle
                    pass

                # not implemented yet
                # impulse_left = int.from_bytes(data[2:4], 'big')

            elif response.arbitration_id == 833:
                self.ui.rangefinderValueLabel.setText(
                    str(int.from_bytes(data[0:2], 'big'))
                )
                temperature = (
                    int.from_bytes(data[2:4], 'big', signed=True) / 10
                    )
                self.ui.tempGraphValueLabel.setText(
                    str(temperature)
                )
                self.ui.factDurationValueLabel.setText(
                    str(int.from_bytes(data[6:], 'big'))
                )
                self.temp_graph.series.append(
                    self.temp_graph.position, temperature
                )
                self.temp_graph.value_list.append(temperature)

            elif response.arbitration_id == 834:
                self.ui.currentValueDoubleSpinBox.setMaximum(
                    int.from_bytes(data[0:2], 'big') / 10
                )
                self.ui.currentSlider.setMaximum(
                    int.from_bytes(data[0:2], 'big')
                )
                self.ui.currentMaxLabel.setText(
                    str(int.from_bytes(data[0:2], 'big') / 10)
                )
                self.ui.durationValueSpinBox.setMaximum(
                    int.from_bytes(data[2:4], 'big')
                )
                self.ui.durationSlider.setMaximum(
                    int.from_bytes(data[2:4], 'big')
                )
                self.ui.durationMaxLabel.setText(
                    str(int.from_bytes(data[2:4], 'big'))
                )
                self.ui.voltageValueDoubleSpinBox.setMinimum(
                    int.from_bytes(data[4:6], 'big') / 10
                )
                self.ui.voltageValueDoubleSpinBox.setMaximum(
                    int.from_bytes(data[6:], 'big') / 10
                )

            elif response.arbitration_id == 835:
                min_pulse_period = int.from_bytes(data[0:3], 'big')
                max_frequency = int(1 / min_pulse_period * 10**6)
                self.ui.frequencyValueSpinBox.setMaximum(max_frequency)
                self.ui.frequencySlider.setMaximum(max_frequency)
                self.ui.frequencyMaxLabel.setText(str(max_frequency))
                # not implemented yet
                # max_tec_voltage = int.from_bytes(data[3], 'big')

            elif response.arbitration_id == 836:
                # the same as 813
                self.ui.currentValueDoubleSpinBox.setValue(
                    int.from_bytes(data[0:2], 'big') / 10
                )
                self.ui.durationValueSpinBox.setValue(
                    int.from_bytes(data[2:4], 'big')
                )
                self.ui.voltageValueDoubleSpinBox.setValue(
                    int.from_bytes(data[4:6], 'big') / 10
                )
                # not implemented yet
                # safe_mode = data[6]

            elif response.arbitration_id == 837:
                # the same as 814
                tec_mode = data[0]
                if tec_mode == 0:
                    self.ui.offTempRadioButton.setChecked(True)
                elif tec_mode == 1:
                    self.ui.stabTempRadioButton.setChecked(True)
                elif tec_mode == 2:
                    self.ui.rangeTempRadioButton.setChecked(True)
                self.ui.stabTempDoubleSpinBox.setValue(
                    int.from_bytes(data[1:3], 'big', signed=True) / 10
                )
                self.ui.rangeTempMaxSpinBox.setValue(
                    int.from_bytes(data[3:4], 'big', signed=True)
                )
                self.ui.rangeTempMinSpinBox.setValue(
                    int.from_bytes(data[4:5], 'big', signed=True)
                )

            elif response.arbitration_id == 838:
                # the same as 815
                self.ui.PCDCheckBox.setChecked(data[0])
                self.ui.PWMValueSpinBox.setValue(data[1])
                self.ui.delayValueSpinBox.setValue(
                    int.from_bytes(data[2:3], 'big', signed=True)
                )
                self.ui.rangefinderCheckBox.setChecked(data[3])

            elif response.arbitration_id == 839:
                # the same as 816
                self.ui.jitterStabCheckBox.setChecked(data[0])
                self.ui.offFDPumpingCheckBox.setChecked(data[1])
                # not implemented yet
                # current_addition = data[2]
                # current_addition_value = int.from_bytes(data[3:5],'big') / 10
                # current_addition_time = data[5]

            elif response.arbitration_id == 840:
                # the same as 817
                # not implemented yet
                # pid_p = int.from_bytes(data[0:2], 'big')
                # pid_i = int.from_bytes(data[2:4], 'big')
                # pid_d = int.from_bytes(data[4:6], 'big')
                # max_cooling_voltage = data[6]
                # max_heating_voltage = data[7]
                pass

            elif response.arbitration_id == 841:
                # the same as 818
                # reserved
                pass

    def set_highlighting(self, widget: QWidget):
        widget.setStyleSheet(
            u"QSpinBox { color: rgb(159, 0, 0); }"
            u"QDoubleSpinBox { color: rgb(159, 0, 0); }"
        )

    def reset_highlighting(self):
        self.ui.currentValueDoubleSpinBox.setStyleSheet(u"")
        self.ui.durationValueSpinBox.setStyleSheet(u"")
        self.ui.frequencyValueSpinBox.setStyleSheet(u"")
        self.ui.voltageValueDoubleSpinBox.setStyleSheet(u"")
        self.ui.delayValueSpinBox.setStyleSheet(u"")
        self.ui.PWMValueSpinBox.setStyleSheet(u"")
        self.ui.stabTempDoubleSpinBox.setStyleSheet(u"")
        self.ui.rangeTempMinSpinBox.setStyleSheet(u"")
        self.ui.rangeTempMaxSpinBox.setStyleSheet(u"")

    def can_receive(self):
        if can_connection_event.is_set():
            print('CAN receiver thread has started')
            while can_connection_event.is_set():
                self.can_parser()

    def closeEvent(self, event):
        if can_connection_event.is_set():
            can_connection_event.clear()
            time.sleep(0.1)
            bus.shutdown()
            if os.name == 'posix':
                password = 'woodman'
                os.system(f"echo {password} "
                          f"| sudo -S ip link set {can_settings.channel} down")
            print("CAN BUS shutdown!")

        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
