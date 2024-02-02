
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
settings_files = [f for f in listdir(settings_path)
                  if (f.endswith('json') and not f.startswith('power'))]

# Make power supply settings first in the settings list
with open('settings/power_supply_settings.json') as f:
    settings = [Munch.fromDict(json.load(f))]

# Add laser preset to the  settings list
for file in settings_files:
    with open(settings_path + file) as f:
        json_dict = json.load(f)
        settings.append(Munch.fromDict(json_dict))
settings = settings

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
        for device in settings:
            self.ui.presetComboBox.addItem(device.name)

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

        # Get power supply capabilities
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

    def on_current_spinbox_value_changed(self):
        self.ui.currentSlider.setValue(
            int(self.ui.currentValueDoubleSpinBox.value() * 10)
        )

    def on_current_slider_value_change(self):
        self.ui.currentValueDoubleSpinBox.setValue(
            self.ui.currentSlider.value() / 10
        )

    def load_device(self, index):
        device = settings[index]

        # CURRENT #
        self.ui.currentValueDoubleSpinBox.setValue(
            device.current.current
        )
        self.ui.currentValueDoubleSpinBox.setMinimum(
            device.current.min_current
        )
        self.ui.currentValueDoubleSpinBox.setMaximum(
            device.current.max_current
        )
        self.ui.currentSlider.setValue(
            device.current.current * 10
        )
        self.ui.currentSlider.setMinimum(
            device.current.min_current * 10
        )
        self.ui.currentSlider.setMaximum(
            device.current.max_current * 10
        )
        self.ui.currentMinLabel.setText(
            str(device.current.min_current)
        )
        self.ui.currentMaxLabel.setText(
            str(device.current.max_current)
        )

        # DURATION #
        self.ui.durationValueSpinBox.setValue(
            device.duration.duration
        )
        self.ui.durationValueSpinBox.setMinimum(
            device.duration.min_duration
        )
        self.ui.durationValueSpinBox.setMaximum(
            device.duration.max_duration
        )
        self.ui.durationSlider.setMinimum(
            device.duration.min_duration
        )
        self.ui.durationSlider.setMaximum(
            device.duration.max_duration
        )
        self.ui.durationMinLabel.setText(
            str(device.duration.min_duration)
        )
        self.ui.durationMaxLabel.setText(
            str(device.duration.max_duration)
        )

        # FREQUENCY #
        self.ui.frequencyValueSpinBox.setValue(
            device.frequency.frequency
        )
        self.ui.frequencyValueSpinBox.setMinimum(
            device.frequency.min_frequency
        )
        self.ui.frequencyValueSpinBox.setMaximum(
            device.frequency.max_frequency
        )
        self.ui.frequencySlider.setMinimum(
            device.frequency.min_frequency
        )
        self.ui.frequencySlider.setMaximum(
            device.frequency.max_frequency
        )
        self.ui.frequencyMinLabel.setText(
            str(device.frequency.min_frequency)
        )
        self.ui.frequencyMaxLabel.setText(
            str(device.frequency.max_frequency)
        )
        self.ui.factDurationValueLabel.setText('none')

        device.frequency.pulse_period_mks = (
            int(1 / self.ui.frequencyValueSpinBox.value() * 10**6)
        )

        # VOLTAGE #
        self.ui.voltageValueDoubleSpinBox.setValue(
            device.voltage.voltage
        )
        self.ui.voltageValueDoubleSpinBox.setMinimum(
            device.voltage.min_voltage
        )
        self.ui.voltageValueDoubleSpinBox.setMaximum(
            device.voltage.max_voltage
        )

        # QSWITCH #
        self.ui.delayValueSpinBox.setValue(
            device.qswitch.delay
        )
        self.ui.delayValueSpinBox.setMinimum(
            device.qswitch.min_delay
        )
        self.ui.delayValueSpinBox.setMaximum(
            device.qswitch.max_delay
        )
        self.ui.PWMValueSpinBox.setValue(
            device.qswitch.pwm
        )

        # RANGE FINDER #
        self.ui.randefinderValueLabel.setText('0')
        self.ui.rangefinderCheckBox.setChecked(
            device.range_finder.mode
        )

        # TEC #
        self.ui.stabTempDoubleSpinBox.setValue(
            device.tec.stabilization_temp
        )
        self.ui.stabTempDoubleSpinBox.setMinimum(
            device.tec.min_stabilization_temp
        )
        self.ui.stabTempDoubleSpinBox.setMaximum(
            device.tec.max_stabilization_temp
        )
        self.ui.rangeTempMinSpinBox.setValue(
            device.tec.min_range_temp
        )
        self.ui.rangeTempMinSpinBox.setMinimum(
            device.tec.min_stabilization_temp
        )
        self.ui.rangeTempMinSpinBox.setMaximum(
            device.tec.max_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setValue(
            device.tec.max_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setMinimum(
            device.tec.min_range_temp
        )
        self.ui.rangeTempMaxSpinBox.setMaximum(
            device.tec.max_stabilization_temp
        )
        self.ui.tempGraphValueLabel.setText(
            str(device.tec.current_temp)
        )

        if device.tec.tec_mode == 0:
            self.ui.offTempRadioButton.click()
        elif device.tec.tec_mode == 1:
            self.ui.stabTempRadioButton.click()
        elif device.tec.tec_mode == 2:
            self.ui.rangeTempRadioButton.click()

        # FEATURES #
        self.ui.PCDCheckBox.setChecked(
            device.features.pcd_21
        )
        self.ui.jitterStabCheckBox.setChecked(
            device.features.jitter_stabilizer
        )
        self.ui.offFDPumpingCheckBox.setChecked(
            device.features.stop_diode
        )

    def prepare_settings_values(self, index):
        device = settings[index]
        device.current.current = self.ui.currentValueDoubleSpinBox.value()
        device.duration.duration = self.ui.durationValueSpinBox.value()
        device.frequency.frequency = self.ui.frequencyValueSpinBox.value()
        device.voltage.voltage = self.ui.voltageValueDoubleSpinBox.value()
        device.qswitch.delay = self.ui.delayValueSpinBox.value()
        device.qswitch.pwm = self.ui.PWMValueSpinBox.value()
        device.features.pcd_21 = self.ui.PCDCheckBox.isChecked()
        device.features.jitter_stabilizer = (
            self.ui.jitterStabCheckBox.isChecked()
            )
        device.features.stop_diode = self.ui.offFDPumpingCheckBox.isChecked()
        device.range_finder.mode = self.ui.rangefinderCheckBox.isChecked()
        if self.ui.offTempRadioButton.isChecked():
            device.tec.tec_mode = 0
        elif self.ui.stabTempRadioButton.isChecked():
            device.tec.tec_mode = 1
        elif self.ui.rangeTempRadioButton.isChecked():
            device.tec.tec_mode = 2
        device.tec.stabilization_temp = self.ui.stabTempDoubleSpinBox.value()
        device.tec.min_range_temp = self.ui.rangeTempMinSpinBox.value()
        device.tec.max_range_temp = self.ui.rangeTempMaxSpinBox.value()

    def on_preset_push_button_pressed(self):
        index = self.ui.presetComboBox.currentIndex()
        self.prepare_settings_values(index)
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
