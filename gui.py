
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_mainWindow
from os import listdir
import os
import json
from munch import Munch
import can

password = 'woodman'
os.system(f"echo {password} "
          "| sudo ip link set can0 up type can bitrate 500000")

settings_path = 'settings/'
settings_files = [f for f in listdir(settings_path) if f.endswith('json')]
settings = []
for file in settings_files:
    with open(settings_path + file) as f:
        json_dict = json.load(f)
        settings.append(Munch.fromDict(json_dict))

interface = 'socketcan'
channel = 'can0'
bitrate = 500000

bus = can.ThreadSafeBus(interface=interface,
                        channel=channel,
                        bitrate=bitrate)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the ui file #
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("images/logoColor.ico"))

        # Hide widgets wich are not active
        self.ui.durationFrame.hide()
        self.ui.frequencyFrame.hide()
        self.ui.connectIconLabel.hide()

        # Default text labels
        self.ui.powerSupplyNumberLabel.setText('Нет соединения')

        # Fill presetComboBox
        self.ui.presetComboBox.clear()
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

        # Load settings for the first(zero index) device
        self.load_device(index=0)

        # Connections #
        self.ui.presetComboBox.currentIndexChanged.connect(
            lambda: self.load_device(self.ui.presetComboBox.currentIndex())
        )
        self.ui.presetPushButton.pressed.connect(
            self.on_preset_push_button_pressed
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
        self.ui.factDurationValueLabel.setText(
            str(int(1 / self.ui.frequencyValueSpinBox.value() * 10**6))
        )
        device.frequency.pulse_period_mks = (
            int(self.ui.factDurationValueLabel.text())
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
