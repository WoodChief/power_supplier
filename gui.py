
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_mainWindow
from os import listdir
import os
import json
from munch import Munch
import can
import threading


with open('CAN.json') as f:
    json_dict = json.load(f)
    can_settings = Munch.fromDict(json_dict)

password = 'woodman'
os.system(f"echo {password} "
          f"| sudo -S ip link set {can_settings.channel} up "
          f"type can bitrate {can_settings.bitrate}")

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
    with open(settings_path + file) as f:
        json_dict = json.load(f)
        settings.append(Munch.fromDict(json_dict))

bus = can.ThreadSafeBus(interface=can_settings.interface,
                        channel=can_settings.channel,
                        bitrate=can_settings.bitrate)
mes = can.Message()
mes.is_extended_id = can_settings.extended_id
mes.dlc = can_settings.dlc


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the ui file #
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("images/logoColor.ico"))

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
        for dev in settings:
            self.ui.presetComboBox.addItem(dev.name)

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

        # Load power supply settings
        self.load_device(0)

        # Get power supply capabilities and correct settings
        self.get_saved_settings()

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

    def on_frequency_button_pressed(self, increment):
        self.ui.frequencyValueSpinBox.setValue(
            self.ui.frequencyValueSpinBox.value() + increment
        )

    def on_duration_button_pressed(self, increment):
        self.ui.durationValueSpinBox.setValue(
            self.ui.durationValueSpinBox.value() + increment
        )

    def on_current_button_pressed(self, increment):
        self.ui.currentValueDoubleSpinBox.setValue(
            self.ui.currentValueDoubleSpinBox.value() + increment
        )

    def on_current_spinbox_value_changed(self):
        self.ui.currentSlider.setValue(
            int(self.ui.currentValueDoubleSpinBox.value() * 10)
        )

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
        with open(file, 'w') as f:
            json.dump(settings[index], f, ensure_ascii=False)

    def on_send_push_button_pressed(self):
        pass

    def on_save_push_button_pressed(self):
        command = can_settings.command.save_current_settings
        mes.arbitration_id = command.mes_id
        mes.data = [command.byte0]
        bus.send(mes)

    def get_saved_settings(self):
        command = can_settings.command.get_saved_settings
        mes.arbitration_id = command.mes_id
        mes.data = [command.byte0]
        bus.send(mes)

    def can_parser(self):
        response = bus.recv(0.02)
        if response is not None:
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
                self.ui.tempGraphValueLabel.setText(
                    str(int.from_bytes(data[2:4], 'big', signed=True) / 10)
                )
                self.ui.factDurationValueLabel.setText(
                    str(int.from_bytes(data[6:], 'big'))
                )

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

    def can_receive(self):
        print('CAN receiver thread has started')
        while True:
            self.can_parser()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
