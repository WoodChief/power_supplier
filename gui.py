
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_mainWindow
from os import listdir
import json
from munch import Munch

settings_path = 'settings/'
settings_files = [f for f in listdir(settings_path) if f.endswith('json')]
settings = []
for file in settings_files:
    with open(settings_path + file) as f:
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

        # Hide sliders wich are not active
        self.ui.durationFrame.hide()
        self.ui.frequencyFrame.hide()

        # Fill presetComboBox
        self.ui.presetComboBox.clear()
        for device in settings:
            self.ui.presetComboBox.addItem(device.name)

        # Connect doubleSpinbox and Slider
        self.ui.currentValueDoubleSpinBox.valueChanged.connect(
            self.on_current_spinbox_value_changed
        )
        self.ui.currentSlider.valueChanged.connect(
            self.on_current_slider_value_change
        )

        # Load settings for the first(zero index) device
        self.load_device(index=0)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
