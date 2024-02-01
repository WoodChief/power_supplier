# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpinBox, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(340, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(340, 580))
        mainWindow.setMaximumSize(QSize(340, 580))
        font = QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 12px;\n"
"	border: 1px solid #969696;\n"
"	background-color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 1px solid #009FA8;\n"
"}\n"
"\n"
"QPushButton::pressed:hover {\n"
"	background-color: #D3DDE0;\n"
"	border: 1px solid #009FA8;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	spacing: 7px;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QCheckBox::unchecked:hover {\n"
"	color: rgb(0, 159, 168);\n"
"}\n"
"QCheckBox:unchecked {\n"
"	color: #666666;\n"
"}\n"
"QCheckBox:checked {\n"
"	color: #000000;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	border: 1px solid #666666;\n"
"	border-radius: 4px;\n"
"	background: #E2E2E2;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color: #009FA8;\n"
"	border-color: #181199;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border-color: rgb(0, 159, 168);\n"
"}\n"
"\n"
"QDoubleSpinBox,\n"
"QSpinBox {\n"
"	border-radius: 6px;\n"
""
                        "	padding-bottom: 1 px;\n"
"	padding-left: 1 px;\n"
"	color: #666666;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover,\n"
"QSpinBox:hover {\n"
"	color: #000000;\n"
"	border: 1px solid#009FA8;\n"
"	padding-bottom: 2 px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #666666;\n"
"}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.durationFrame = QFrame(self.centralwidget)
        self.durationFrame.setObjectName(u"durationFrame")
        self.durationFrame.setGeometry(QRect(30, 165, 270, 70))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Light"])
        font1.setPointSize(9)
        self.durationFrame.setFont(font1)
        self.durationFrame.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #EDEDED;\n"
"	background-color: #EDEDED;\n"
"	color: #666666;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #009FA8;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #D3DDE0;\n"
"}")
        self.durationFrame.setFrameShape(QFrame.StyledPanel)
        self.durationFrame.setFrameShadow(QFrame.Raised)
        self.durationSlider = QSlider(self.durationFrame)
        self.durationSlider.setObjectName(u"durationSlider")
        self.durationSlider.setGeometry(QRect(30, 10, 205, 22))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Light"])
        self.durationSlider.setFont(font2)
        self.durationSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 6px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"	border-radius: 3px;\n"
"	margin-left: 1px;\n"
"	margin-right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #009FA8;\n"
"	width: 12px;\n"
"	margin: -4px -1px;\n"
"    border-radius: 7px;\n"
"	border: 1px solid #009FA8;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #009FA8;\n"
"	border-color: #181199;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background: qlineargradient(x1:1, y1:0.5, x2:0, y2:0.5, stop:0 #009FA8, stop:1 #181199);\n"
"	border-radius: 3px;\n"
"}")
        self.durationSlider.setMinimum(1)
        self.durationSlider.setMaximum(250)
        self.durationSlider.setSingleStep(5)
        self.durationSlider.setValue(220)
        self.durationSlider.setSliderPosition(220)
        self.durationSlider.setOrientation(Qt.Horizontal)
        self.durationMinusTenPushButton = QPushButton(self.durationFrame)
        self.durationMinusTenPushButton.setObjectName(u"durationMinusTenPushButton")
        self.durationMinusTenPushButton.setGeometry(QRect(90, 40, 30, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.durationMinusTenPushButton.sizePolicy().hasHeightForWidth())
        self.durationMinusTenPushButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Light"])
        font3.setPointSize(10)
        self.durationMinusTenPushButton.setFont(font3)
        self.durationMinusTenPushButton.setStyleSheet(u"")
        self.durationPlusTwentyPushButton = QPushButton(self.durationFrame)
        self.durationPlusTwentyPushButton.setObjectName(u"durationPlusTwentyPushButton")
        self.durationPlusTwentyPushButton.setGeometry(QRect(205, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.durationPlusTwentyPushButton.sizePolicy().hasHeightForWidth())
        self.durationPlusTwentyPushButton.setSizePolicy(sizePolicy1)
        self.durationPlusTwentyPushButton.setFont(font3)
        self.durationPlusTwentyPushButton.setStyleSheet(u"")
        self.durationMinusTwentyPushButton = QPushButton(self.durationFrame)
        self.durationMinusTwentyPushButton.setObjectName(u"durationMinusTwentyPushButton")
        self.durationMinusTwentyPushButton.setGeometry(QRect(30, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.durationMinusTwentyPushButton.sizePolicy().hasHeightForWidth())
        self.durationMinusTwentyPushButton.setSizePolicy(sizePolicy1)
        self.durationMinusTwentyPushButton.setFont(font3)
        self.durationMinusTwentyPushButton.setStyleSheet(u"")
        self.durationMaxLabel = QLabel(self.durationFrame)
        self.durationMaxLabel.setObjectName(u"durationMaxLabel")
        self.durationMaxLabel.setGeometry(QRect(248, 11, 21, 16))
        self.durationMaxLabel.setFont(font2)
        self.durationPlusTenPushButton = QPushButton(self.durationFrame)
        self.durationPlusTenPushButton.setObjectName(u"durationPlusTenPushButton")
        self.durationPlusTenPushButton.setGeometry(QRect(147, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.durationPlusTenPushButton.sizePolicy().hasHeightForWidth())
        self.durationPlusTenPushButton.setSizePolicy(sizePolicy1)
        self.durationPlusTenPushButton.setFont(font3)
        self.durationPlusTenPushButton.setStyleSheet(u"")
        self.durationMinLabel = QLabel(self.durationFrame)
        self.durationMinLabel.setObjectName(u"durationMinLabel")
        self.durationMinLabel.setGeometry(QRect(5, 11, 16, 16))
        self.durationMinLabel.setFont(font2)
        self.currentDurationFrequencyFrame = QFrame(self.centralwidget)
        self.currentDurationFrequencyFrame.setObjectName(u"currentDurationFrequencyFrame")
        self.currentDurationFrequencyFrame.setGeometry(QRect(30, 40, 220, 115))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Light"])
        font4.setPointSize(12)
        self.currentDurationFrequencyFrame.setFont(font4)
        self.currentDurationFrequencyFrame.setStyleSheet(u"QRadioButton::indicator {\n"
"	width:0 ;\n"
"	height:0;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	text-align: left;\n"
"	padding-left: 7 px;\n"
"	padding-bottom: 2 px;\n"
"	color: #666666;\n"
"	border: 1px solid #969696;\n"
"	border-right: none;\n"
"	background-color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"QRadioButton::clicked,\n"
"QRadioButton::checked {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0, stop:0 rgba(24, 17, 153, 255), stop:1 rgba(0, 159, 168, 255));\n"
"	border: none;\n"
"	color: white;\n"
"	padding-left: 8 px;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: #000000;\n"
"	border: 1px solid rgb(0, 159, 168);\n"
"}\n"
"\n"
"QRadioButton::clicked:hover,\n"
"QRadioButton::checked:hover{\n"
"	color: white;\n"
"	border: none;\n"
"}\n"
"\n"
"QDoubleSpinBox,\n"
"QSpinBox {\n"
"	border: 1px solid #969696;\n"
"	border-left: none;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"	border-top"
                        "-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background-color: rgb(237, 237, 237);\n"
"	padding-bottom: 2px;\n"
"	padding-left: 10px;\n"
"	color: #666666;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover,\n"
"QSpinBox:hover {\n"
"	border: 1px solid rgb(0, 159, 168);\n"
"	color: #000000;\n"
"	background-color: rgb(230, 237, 239);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 1px solid #969696;\n"
"	border-top: none;\n"
"	border-bottom: none;\n"
"	border-right: none;\n"
"}")
        self.currentDurationFrequencyFrame.setFrameShape(QFrame.StyledPanel)
        self.currentDurationFrequencyFrame.setFrameShadow(QFrame.Raised)
        self.durationRadioButton = QRadioButton(self.currentDurationFrequencyFrame)
        self.durationRadioButton.setObjectName(u"durationRadioButton")
        self.durationRadioButton.setGeometry(QRect(10, 45, 150, 25))
        font5 = QFont()
        font5.setFamilies([u"Yu Gothic UI Light"])
        font5.setPointSize(11)
        self.durationRadioButton.setFont(font5)
        self.durationRadioButton.setStyleSheet(u"")
        self.durationRadioButton.setCheckable(True)
        self.currentRadioButton = QRadioButton(self.currentDurationFrequencyFrame)
        self.currentRadioButton.setObjectName(u"currentRadioButton")
        self.currentRadioButton.setGeometry(QRect(10, 10, 150, 25))
        self.currentRadioButton.setFont(font5)
        self.currentRadioButton.setStyleSheet(u"")
        self.currentRadioButton.setCheckable(True)
        self.currentRadioButton.setChecked(True)
        self.frequencyRadioButton = QRadioButton(self.currentDurationFrequencyFrame)
        self.frequencyRadioButton.setObjectName(u"frequencyRadioButton")
        self.frequencyRadioButton.setGeometry(QRect(10, 80, 150, 25))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frequencyRadioButton.sizePolicy().hasHeightForWidth())
        self.frequencyRadioButton.setSizePolicy(sizePolicy2)
        self.frequencyRadioButton.setFont(font5)
        self.frequencyRadioButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.frequencyRadioButton.setLayoutDirection(Qt.LeftToRight)
        self.frequencyRadioButton.setStyleSheet(u"")
        self.frequencyRadioButton.setCheckable(True)
        self.frequencyValueSpinBox = QSpinBox(self.currentDurationFrequencyFrame)
        self.frequencyValueSpinBox.setObjectName(u"frequencyValueSpinBox")
        self.frequencyValueSpinBox.setGeometry(QRect(159, 80, 50, 25))
        self.frequencyValueSpinBox.setFont(font5)
        self.frequencyValueSpinBox.setStyleSheet(u"")
        self.frequencyValueSpinBox.setFrame(False)
        self.frequencyValueSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.frequencyValueSpinBox.setMinimum(1)
        self.frequencyValueSpinBox.setMaximum(50)
        self.frequencyValueSpinBox.setValue(25)
        self.durationValueSpinBox = QSpinBox(self.currentDurationFrequencyFrame)
        self.durationValueSpinBox.setObjectName(u"durationValueSpinBox")
        self.durationValueSpinBox.setGeometry(QRect(159, 45, 50, 25))
        self.durationValueSpinBox.setFont(font5)
        self.durationValueSpinBox.setStyleSheet(u"")
        self.durationValueSpinBox.setFrame(False)
        self.durationValueSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.durationValueSpinBox.setMinimum(20)
        self.durationValueSpinBox.setMaximum(600)
        self.durationValueSpinBox.setValue(220)
        self.currentValueDoubleSpinBox = QDoubleSpinBox(self.currentDurationFrequencyFrame)
        self.currentValueDoubleSpinBox.setObjectName(u"currentValueDoubleSpinBox")
        self.currentValueDoubleSpinBox.setGeometry(QRect(159, 10, 50, 25))
        self.currentValueDoubleSpinBox.setFont(font5)
        self.currentValueDoubleSpinBox.setStyleSheet(u"")
        self.currentValueDoubleSpinBox.setFrame(False)
        self.currentValueDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.currentValueDoubleSpinBox.setDecimals(1)
        self.currentValueDoubleSpinBox.setMaximum(230.000000000000000)
        self.currentValueDoubleSpinBox.setSingleStep(0.500000000000000)
        self.currentValueDoubleSpinBox.setValue(70.000000000000000)
        self.durationLineLabel = QLabel(self.currentDurationFrequencyFrame)
        self.durationLineLabel.setObjectName(u"durationLineLabel")
        self.durationLineLabel.setGeometry(QRect(159, 50, 5, 15))
        self.frequencyLineLabel = QLabel(self.currentDurationFrequencyFrame)
        self.frequencyLineLabel.setObjectName(u"frequencyLineLabel")
        self.frequencyLineLabel.setGeometry(QRect(159, 85, 5, 15))
        self.currentLineLabel = QLabel(self.currentDurationFrequencyFrame)
        self.currentLineLabel.setObjectName(u"currentLineLabel")
        self.currentLineLabel.setGeometry(QRect(159, 15, 5, 15))
        self.frequencyValueSpinBox.raise_()
        self.currentValueDoubleSpinBox.raise_()
        self.durationValueSpinBox.raise_()
        self.durationRadioButton.raise_()
        self.currentRadioButton.raise_()
        self.currentLineLabel.raise_()
        self.durationLineLabel.raise_()
        self.frequencyRadioButton.raise_()
        self.frequencyLineLabel.raise_()
        self.startStopFrame = QFrame(self.centralwidget)
        self.startStopFrame.setObjectName(u"startStopFrame")
        self.startStopFrame.setGeometry(QRect(20, 235, 300, 60))
        self.startStopFrame.setFont(font2)
        self.startStopFrame.setLayoutDirection(Qt.LeftToRight)
        self.startStopFrame.setAutoFillBackground(False)
        self.startStopFrame.setStyleSheet(u"QRadioButton::indicator {\n"
"	width:0 ;\n"
"	height:0;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	text-align: left;\n"
"	padding-left: 22px;\n"
"	padding-bottom: 1 px;\n"
"	color: #969696;\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::clicked,\n"
"QRadioButton::checked {\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton::clicked:hover,\n"
"QRadioButton::checked:hover{\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"	color: rgb(0, 159, 168);\n"
"}\n"
"")
        self.startStopFrame.setFrameShape(QFrame.StyledPanel)
        self.startStopFrame.setFrameShadow(QFrame.Raised)
        self.stopRadioButton = QRadioButton(self.startStopFrame)
        self.stopRadioButton.setObjectName(u"stopRadioButton")
        self.stopRadioButton.setGeometry(QRect(10, 10, 100, 40))
        font6 = QFont()
        font6.setFamilies([u"Yu Gothic UI Semibold"])
        font6.setPointSize(11)
        self.stopRadioButton.setFont(font6)
        self.stopRadioButton.setStyleSheet(u"QRadioButton{\n"
"	padding-left: 22px;\n"
"}\n"
"\n"
"QRadioButton::clicked,\n"
"QRadioButton::checked {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #961128, stop:1 #181199);\n"
"}")
        self.stopRadioButton.setChecked(True)
        self.startRadioButton = QRadioButton(self.startStopFrame)
        self.startRadioButton.setObjectName(u"startRadioButton")
        self.startRadioButton.setGeometry(QRect(100, 10, 100, 40))
        self.startRadioButton.setFont(font6)
        self.startRadioButton.setStyleSheet(u"QRadioButton{\n"
"	padding-left: 22px;\n"
"}\n"
"\n"
"QRadioButton::clicked,\n"
"QRadioButton::checked {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #181199, stop:1 #0B61A1);\n"
"}")
        self.backgroudStartStopLabel = QLabel(self.startStopFrame)
        self.backgroudStartStopLabel.setObjectName(u"backgroudStartStopLabel")
        self.backgroudStartStopLabel.setGeometry(QRect(10, 10, 280, 40))
        self.backgroudStartStopLabel.setStyleSheet(u"QLabel {\n"
"	border-radius: 20px;\n"
"	border: 1px solid #009FA8;\n"
"	background-color: #E2E2E2;\n"
"}\n"
"")
        self.externalTriggerRadioButton = QRadioButton(self.startStopFrame)
        self.externalTriggerRadioButton.setObjectName(u"externalTriggerRadioButton")
        self.externalTriggerRadioButton.setGeometry(QRect(190, 10, 100, 40))
        font7 = QFont()
        font7.setFamilies([u"Yu Gothic UI Semibold"])
        font7.setPointSize(9)
        self.externalTriggerRadioButton.setFont(font7)
        self.externalTriggerRadioButton.setLayoutDirection(Qt.LeftToRight)
        self.externalTriggerRadioButton.setStyleSheet(u"QRadioButton{\n"
"	padding-left: 15px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QRadioButton::clicked,\n"
"QRadioButton::checked {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #0B61A1, stop:1 #009FA8);\n"
"}")
        self.backgroudStartStopLabel.raise_()
        self.stopRadioButton.raise_()
        self.startRadioButton.raise_()
        self.externalTriggerRadioButton.raise_()
        self.backgroundCurrentDurationFrequencyLabel = QLabel(self.centralwidget)
        self.backgroundCurrentDurationFrequencyLabel.setObjectName(u"backgroundCurrentDurationFrequencyLabel")
        self.backgroundCurrentDurationFrequencyLabel.setGeometry(QRect(20, 40, 300, 115))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.backgroundCurrentDurationFrequencyLabel.sizePolicy().hasHeightForWidth())
        self.backgroundCurrentDurationFrequencyLabel.setSizePolicy(sizePolicy3)
        self.backgroundCurrentDurationFrequencyLabel.setStyleSheet(u"QLabel {\n"
"	background-color: #E2E2E2;\n"
"	border-radius: 15px;\n"
"}")
        self.backgroundSliderLabel = QLabel(self.centralwidget)
        self.backgroundSliderLabel.setObjectName(u"backgroundSliderLabel")
        self.backgroundSliderLabel.setGeometry(QRect(20, 165, 300, 70))
        self.backgroundSliderLabel.setStyleSheet(u"QLabel {\n"
"	background-color: #E2E2E2;\n"
"	border-radius: 15px;\n"
"}")
        self.frequencyFrame = QFrame(self.centralwidget)
        self.frequencyFrame.setObjectName(u"frequencyFrame")
        self.frequencyFrame.setGeometry(QRect(30, 165, 270, 70))
        self.frequencyFrame.setFont(font1)
        self.frequencyFrame.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #EDEDED;\n"
"	background-color: #EDEDED;\n"
"	color: #666666;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #009FA8;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #D3DDE0;\n"
"}")
        self.frequencyFrame.setFrameShape(QFrame.StyledPanel)
        self.frequencyFrame.setFrameShadow(QFrame.Raised)
        self.frequencySlider = QSlider(self.frequencyFrame)
        self.frequencySlider.setObjectName(u"frequencySlider")
        self.frequencySlider.setGeometry(QRect(30, 10, 205, 22))
        self.frequencySlider.setFont(font2)
        self.frequencySlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 6px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"	border-radius: 3px;\n"
"	margin-left: 1px;\n"
"	margin-right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #009FA8;\n"
"	width: 12px;\n"
"	margin: -4px -1px;\n"
"    border-radius: 7px;\n"
"	border: 1px solid #009FA8;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #009FA8;\n"
"	border-color: #181199;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background: qlineargradient(x1:1, y1:0.5, x2:0, y2:0.5, stop:0 #009FA8, stop:1 #181199);\n"
"	border-radius: 3px;\n"
"}")
        self.frequencySlider.setMinimum(1)
        self.frequencySlider.setMaximum(50)
        self.frequencySlider.setValue(15)
        self.frequencySlider.setSliderPosition(15)
        self.frequencySlider.setOrientation(Qt.Horizontal)
        self.frequencyMaxLabel = QLabel(self.frequencyFrame)
        self.frequencyMaxLabel.setObjectName(u"frequencyMaxLabel")
        self.frequencyMaxLabel.setGeometry(QRect(250, 11, 16, 16))
        self.frequencyMaxLabel.setFont(font2)
        self.frequencyMinLabel = QLabel(self.frequencyFrame)
        self.frequencyMinLabel.setObjectName(u"frequencyMinLabel")
        self.frequencyMinLabel.setGeometry(QRect(12, 11, 16, 16))
        self.frequencyMinLabel.setFont(font2)
        self.frequencyPlusOnePushButton = QPushButton(self.frequencyFrame)
        self.frequencyPlusOnePushButton.setObjectName(u"frequencyPlusOnePushButton")
        self.frequencyPlusOnePushButton.setGeometry(QRect(147, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.frequencyPlusOnePushButton.sizePolicy().hasHeightForWidth())
        self.frequencyPlusOnePushButton.setSizePolicy(sizePolicy1)
        self.frequencyPlusOnePushButton.setFont(font3)
        self.frequencyPlusOnePushButton.setStyleSheet(u"")
        self.frequencyPlusFivePushButton = QPushButton(self.frequencyFrame)
        self.frequencyPlusFivePushButton.setObjectName(u"frequencyPlusFivePushButton")
        self.frequencyPlusFivePushButton.setGeometry(QRect(205, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.frequencyPlusFivePushButton.sizePolicy().hasHeightForWidth())
        self.frequencyPlusFivePushButton.setSizePolicy(sizePolicy1)
        self.frequencyPlusFivePushButton.setFont(font3)
        self.frequencyPlusFivePushButton.setStyleSheet(u"")
        self.frequencyMinusOnePushButton = QPushButton(self.frequencyFrame)
        self.frequencyMinusOnePushButton.setObjectName(u"frequencyMinusOnePushButton")
        self.frequencyMinusOnePushButton.setGeometry(QRect(90, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.frequencyMinusOnePushButton.sizePolicy().hasHeightForWidth())
        self.frequencyMinusOnePushButton.setSizePolicy(sizePolicy1)
        self.frequencyMinusOnePushButton.setFont(font3)
        self.frequencyMinusOnePushButton.setStyleSheet(u"")
        self.frequencyMinusFivePushButton = QPushButton(self.frequencyFrame)
        self.frequencyMinusFivePushButton.setObjectName(u"frequencyMinusFivePushButton")
        self.frequencyMinusFivePushButton.setGeometry(QRect(30, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.frequencyMinusFivePushButton.sizePolicy().hasHeightForWidth())
        self.frequencyMinusFivePushButton.setSizePolicy(sizePolicy1)
        self.frequencyMinusFivePushButton.setFont(font3)
        self.frequencyMinusFivePushButton.setStyleSheet(u"")
        self.parametersFrame = QFrame(self.centralwidget)
        self.parametersFrame.setObjectName(u"parametersFrame")
        self.parametersFrame.setGeometry(QRect(20, 290, 300, 120))
        self.parametersFrame.setFrameShape(QFrame.StyledPanel)
        self.parametersFrame.setFrameShadow(QFrame.Raised)
        self.parametersLineLabel = QLabel(self.parametersFrame)
        self.parametersLineLabel.setObjectName(u"parametersLineLabel")
        self.parametersLineLabel.setGeometry(QRect(155, 10, 5, 101))
        self.parametersLineLabel.setStyleSheet(u"QLabel {\n"
"	border: 1px solid #009FA8;\n"
"	border-top: none;\n"
"	border-bottom: none;\n"
"	border-right: none;\n"
"}")
        self.factDurationValueLabel = QLabel(self.parametersFrame)
        self.factDurationValueLabel.setObjectName(u"factDurationValueLabel")
        self.factDurationValueLabel.setEnabled(True)
        self.factDurationValueLabel.setGeometry(QRect(108, 73, 38, 16))
        self.factDurationValueLabel.setFont(font1)
        self.factDurationValueLabel.setLayoutDirection(Qt.RightToLeft)
        self.factDurationValueLabel.setAlignment(Qt.AlignCenter)
        self.offFDPumpingCheckBox = QCheckBox(self.parametersFrame)
        self.offFDPumpingCheckBox.setObjectName(u"offFDPumpingCheckBox")
        self.offFDPumpingCheckBox.setGeometry(QRect(167, 70, 131, 21))
        self.offFDPumpingCheckBox.setFont(font1)
        self.voltageLabel = QLabel(self.parametersFrame)
        self.voltageLabel.setObjectName(u"voltageLabel")
        self.voltageLabel.setGeometry(QRect(5, 13, 91, 16))
        self.voltageLabel.setFont(font1)
        self.PCDCheckBox = QCheckBox(self.parametersFrame)
        self.PCDCheckBox.setObjectName(u"PCDCheckBox")
        self.PCDCheckBox.setGeometry(QRect(167, 30, 101, 20))
        self.PCDCheckBox.setFont(font1)
        self.jitterStabCheckBox = QCheckBox(self.parametersFrame)
        self.jitterStabCheckBox.setObjectName(u"jitterStabCheckBox")
        self.jitterStabCheckBox.setGeometry(QRect(167, 50, 111, 20))
        sizePolicy2.setHeightForWidth(self.jitterStabCheckBox.sizePolicy().hasHeightForWidth())
        self.jitterStabCheckBox.setSizePolicy(sizePolicy2)
        self.jitterStabCheckBox.setFont(font1)
        self.jitterStabCheckBox.setStyleSheet(u"")
        self.randefinderValueLabel = QLabel(self.parametersFrame)
        self.randefinderValueLabel.setObjectName(u"randefinderValueLabel")
        self.randefinderValueLabel.setEnabled(True)
        self.randefinderValueLabel.setGeometry(QRect(108, 93, 38, 16))
        self.randefinderValueLabel.setFont(font1)
        self.randefinderValueLabel.setLayoutDirection(Qt.RightToLeft)
        self.randefinderValueLabel.setAlignment(Qt.AlignCenter)
        self.randefinderLabel = QLabel(self.parametersFrame)
        self.randefinderLabel.setObjectName(u"randefinderLabel")
        self.randefinderLabel.setEnabled(True)
        self.randefinderLabel.setGeometry(QRect(5, 93, 91, 16))
        self.randefinderLabel.setFont(font1)
        self.rangefinderCheckBox = QCheckBox(self.parametersFrame)
        self.rangefinderCheckBox.setObjectName(u"rangefinderCheckBox")
        self.rangefinderCheckBox.setGeometry(QRect(167, 90, 131, 21))
        self.rangefinderCheckBox.setFont(font1)
        self.factDurationLabel = QLabel(self.parametersFrame)
        self.factDurationLabel.setObjectName(u"factDurationLabel")
        self.factDurationLabel.setGeometry(QRect(5, 73, 101, 16))
        self.factDurationLabel.setFont(font1)
        self.delayLabel = QLabel(self.parametersFrame)
        self.delayLabel.setObjectName(u"delayLabel")
        self.delayLabel.setGeometry(QRect(5, 33, 91, 16))
        self.delayLabel.setFont(font1)
        self.PWMLabel = QLabel(self.parametersFrame)
        self.PWMLabel.setObjectName(u"PWMLabel")
        self.PWMLabel.setGeometry(QRect(5, 53, 91, 16))
        self.PWMLabel.setFont(font1)
        self.voltageValueDoubleSpinBox = QDoubleSpinBox(self.parametersFrame)
        self.voltageValueDoubleSpinBox.setObjectName(u"voltageValueDoubleSpinBox")
        self.voltageValueDoubleSpinBox.setGeometry(QRect(110, 13, 35, 17))
        self.voltageValueDoubleSpinBox.setFont(font2)
        self.voltageValueDoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.voltageValueDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.voltageValueDoubleSpinBox.setDecimals(1)
        self.voltageValueDoubleSpinBox.setMaximum(200.000000000000000)
        self.voltageValueDoubleSpinBox.setSingleStep(0.500000000000000)
        self.voltageValueDoubleSpinBox.setValue(170.000000000000000)
        self.delayValueSpinBox = QSpinBox(self.parametersFrame)
        self.delayValueSpinBox.setObjectName(u"delayValueSpinBox")
        self.delayValueSpinBox.setGeometry(QRect(110, 33, 35, 17))
        self.delayValueSpinBox.setFont(font2)
        self.delayValueSpinBox.setAlignment(Qt.AlignCenter)
        self.delayValueSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.delayValueSpinBox.setMinimum(-30)
        self.delayValueSpinBox.setMaximum(30)
        self.delayValueSpinBox.setValue(5)
        self.PWMValueSpinBox = QSpinBox(self.parametersFrame)
        self.PWMValueSpinBox.setObjectName(u"PWMValueSpinBox")
        self.PWMValueSpinBox.setGeometry(QRect(110, 53, 35, 17))
        self.PWMValueSpinBox.setFont(font2)
        self.PWMValueSpinBox.setAlignment(Qt.AlignCenter)
        self.PWMValueSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.PWMValueSpinBox.setMaximum(100)
        self.PWMValueSpinBox.setValue(95)
        self.tecFrame = QFrame(self.centralwidget)
        self.tecFrame.setObjectName(u"tecFrame")
        self.tecFrame.setGeometry(QRect(20, 420, 111, 121))
        self.tecFrame.setFont(font3)
        self.tecFrame.setStyleSheet(u"QRadioButton {\n"
"	spacing: 7px;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QRadioButton::unchecked:hover {\n"
"	color: rgb(0, 159, 168);\n"
"}\n"
"\n"
"QRadioButton:unchecked {\n"
"	color: #666666;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color: #000000;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	border: 1px solid #666666;\n"
"	border-radius: 6px;\n"
"	background: #E2E2E2;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: rgba(0, 159, 168, 255);\n"
"	border-color: #181199;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"	border-color: rgb(0, 159, 168);\n"
"}")
        self.tecFrame.setFrameShape(QFrame.StyledPanel)
        self.tecFrame.setFrameShadow(QFrame.Raised)
        self.stabTempRadioButton = QRadioButton(self.tecFrame)
        self.stabTempRadioButton.setObjectName(u"stabTempRadioButton")
        self.stabTempRadioButton.setGeometry(QRect(5, 40, 111, 20))
        self.stabTempRadioButton.setFont(font1)
        self.offTempRadioButton = QRadioButton(self.tecFrame)
        self.offTempRadioButton.setObjectName(u"offTempRadioButton")
        self.offTempRadioButton.setGeometry(QRect(5, 20, 111, 20))
        self.offTempRadioButton.setFont(font1)
        self.offTempRadioButton.setTabletTracking(False)
        self.offTempRadioButton.setAutoFillBackground(False)
        self.rangeTempRadioButton = QRadioButton(self.tecFrame)
        self.rangeTempRadioButton.setObjectName(u"rangeTempRadioButton")
        self.rangeTempRadioButton.setGeometry(QRect(5, 80, 89, 20))
        self.rangeTempRadioButton.setFont(font1)
        self.tecLabel = QLabel(self.tecFrame)
        self.tecLabel.setObjectName(u"tecLabel")
        self.tecLabel.setGeometry(QRect(5, 0, 91, 16))
        font8 = QFont()
        font8.setFamilies([u"Yu Gothic UI Semibold"])
        font8.setPointSize(9)
        font8.setBold(False)
        self.tecLabel.setFont(font8)
        self.tecLabel.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"}")
        self.stabTempDegreesLabel = QLabel(self.tecFrame)
        self.stabTempDegreesLabel.setObjectName(u"stabTempDegreesLabel")
        self.stabTempDegreesLabel.setEnabled(True)
        self.stabTempDegreesLabel.setGeometry(QRect(58, 60, 21, 16))
        self.stabTempDegreesLabel.setFont(font1)
        self.stabTempDegreesLabel.setLayoutDirection(Qt.RightToLeft)
        self.stabTempDegreesLabel.setAlignment(Qt.AlignCenter)
        self.rangeTempHyphenLabel = QLabel(self.tecFrame)
        self.rangeTempHyphenLabel.setObjectName(u"rangeTempHyphenLabel")
        self.rangeTempHyphenLabel.setEnabled(True)
        self.rangeTempHyphenLabel.setGeometry(QRect(46, 100, 16, 16))
        self.rangeTempHyphenLabel.setFont(font1)
        self.rangeTempHyphenLabel.setLayoutDirection(Qt.RightToLeft)
        self.rangeTempHyphenLabel.setAlignment(Qt.AlignCenter)
        self.rangeTempDegreesLabel = QLabel(self.tecFrame)
        self.rangeTempDegreesLabel.setObjectName(u"rangeTempDegreesLabel")
        self.rangeTempDegreesLabel.setEnabled(True)
        self.rangeTempDegreesLabel.setGeometry(QRect(83, 100, 21, 16))
        self.rangeTempDegreesLabel.setFont(font1)
        self.rangeTempDegreesLabel.setLayoutDirection(Qt.RightToLeft)
        self.rangeTempDegreesLabel.setAlignment(Qt.AlignCenter)
        self.stabTempDoubleSpinBox = QDoubleSpinBox(self.tecFrame)
        self.stabTempDoubleSpinBox.setObjectName(u"stabTempDoubleSpinBox")
        self.stabTempDoubleSpinBox.setGeometry(QRect(25, 60, 32, 17))
        self.stabTempDoubleSpinBox.setFont(font2)
        self.stabTempDoubleSpinBox.setAlignment(Qt.AlignCenter)
        self.stabTempDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.stabTempDoubleSpinBox.setDecimals(1)
        self.stabTempDoubleSpinBox.setMaximum(80.000000000000000)
        self.stabTempDoubleSpinBox.setSingleStep(0.100000000000000)
        self.stabTempDoubleSpinBox.setValue(30.000000000000000)
        self.rangeTempMinSpinBox = QSpinBox(self.tecFrame)
        self.rangeTempMinSpinBox.setObjectName(u"rangeTempMinSpinBox")
        self.rangeTempMinSpinBox.setGeometry(QRect(25, 100, 25, 17))
        self.rangeTempMinSpinBox.setFont(font2)
        self.rangeTempMinSpinBox.setAlignment(Qt.AlignCenter)
        self.rangeTempMinSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rangeTempMinSpinBox.setMinimum(-60)
        self.rangeTempMinSpinBox.setMaximum(80)
        self.rangeTempMinSpinBox.setValue(25)
        self.rangeTempMaxSpinBox = QSpinBox(self.tecFrame)
        self.rangeTempMaxSpinBox.setObjectName(u"rangeTempMaxSpinBox")
        self.rangeTempMaxSpinBox.setGeometry(QRect(59, 100, 25, 17))
        self.rangeTempMaxSpinBox.setFont(font2)
        self.rangeTempMaxSpinBox.setAlignment(Qt.AlignCenter)
        self.rangeTempMaxSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rangeTempMaxSpinBox.setMinimum(-60)
        self.rangeTempMaxSpinBox.setMaximum(80)
        self.rangeTempMaxSpinBox.setValue(35)
        self.tempGraphFrame = QFrame(self.centralwidget)
        self.tempGraphFrame.setObjectName(u"tempGraphFrame")
        self.tempGraphFrame.setGeometry(QRect(140, 420, 180, 121))
        self.tempGraphFrame.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #EDEDED;\n"
"	background-color: #EDEDED;\n"
"	color: #666666;\n"
"	padding-bottom: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #009FA8;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #D3DDE0;\n"
"}")
        self.tempGraphFrame.setFrameShape(QFrame.StyledPanel)
        self.tempGraphFrame.setFrameShadow(QFrame.Raised)
        self.tempGraphDegreesLabel = QLabel(self.tempGraphFrame)
        self.tempGraphDegreesLabel.setObjectName(u"tempGraphDegreesLabel")
        self.tempGraphDegreesLabel.setEnabled(True)
        self.tempGraphDegreesLabel.setGeometry(QRect(150, 10, 21, 18))
        self.tempGraphDegreesLabel.setFont(font4)
        self.tempGraphDegreesLabel.setLayoutDirection(Qt.RightToLeft)
        self.tempGraphDegreesLabel.setAlignment(Qt.AlignCenter)
        self.tempGraphValueLabel = QLabel(self.tempGraphFrame)
        self.tempGraphValueLabel.setObjectName(u"tempGraphValueLabel")
        self.tempGraphValueLabel.setEnabled(True)
        self.tempGraphValueLabel.setGeometry(QRect(120, 10, 31, 18))
        self.tempGraphValueLabel.setFont(font4)
        self.tempGraphValueLabel.setLayoutDirection(Qt.RightToLeft)
        self.tempGraphValueLabel.setAlignment(Qt.AlignCenter)
        self.tempGraphPlusPushButton = QPushButton(self.tempGraphFrame)
        self.tempGraphPlusPushButton.setObjectName(u"tempGraphPlusPushButton")
        self.tempGraphPlusPushButton.setGeometry(QRect(50, 10, 30, 20))
        sizePolicy1.setHeightForWidth(self.tempGraphPlusPushButton.sizePolicy().hasHeightForWidth())
        self.tempGraphPlusPushButton.setSizePolicy(sizePolicy1)
        self.tempGraphPlusPushButton.setFont(font3)
        self.tempGraphPlusPushButton.setStyleSheet(u"")
        self.tempGraphMinusPushButton = QPushButton(self.tempGraphFrame)
        self.tempGraphMinusPushButton.setObjectName(u"tempGraphMinusPushButton")
        self.tempGraphMinusPushButton.setGeometry(QRect(10, 10, 30, 20))
        sizePolicy1.setHeightForWidth(self.tempGraphMinusPushButton.sizePolicy().hasHeightForWidth())
        self.tempGraphMinusPushButton.setSizePolicy(sizePolicy1)
        self.tempGraphMinusPushButton.setFont(font3)
        self.tempGraphMinusPushButton.setStyleSheet(u"")
        self.bottomFrame = QFrame(self.centralwidget)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setGeometry(QRect(140, 550, 181, 21))
        self.bottomFrame.setLayoutDirection(Qt.LeftToRight)
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.powerSupplyNumberLabel = QLabel(self.bottomFrame)
        self.powerSupplyNumberLabel.setObjectName(u"powerSupplyNumberLabel")
        self.powerSupplyNumberLabel.setGeometry(QRect(30, 0, 141, 20))
        self.powerSupplyNumberLabel.setFont(font1)
        self.powerSupplyNumberLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.connectIconLabel = QLabel(self.bottomFrame)
        self.connectIconLabel.setObjectName(u"connectIconLabel")
        self.connectIconLabel.setGeometry(QRect(5, 0, 20, 20))
        self.connectIconLabel.setStyleSheet(u"QLabel {\n"
"	border-image: url(images/connect.svg) center;\n"
"}")
        self.disconnectIconLabel = QLabel(self.bottomFrame)
        self.disconnectIconLabel.setObjectName(u"disconnectIconLabel")
        self.disconnectIconLabel.setGeometry(QRect(5, 0, 20, 20))
        self.disconnectIconLabel.setStyleSheet(u"QLabel {\n"
"	border-image: url(images/disconnect.svg) center;\n"
"}")
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setGeometry(QRect(20, 0, 301, 41))
        self.topFrame.setStyleSheet(u"QPushButton {\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px; \n"
"	border-top-left-radius: none;\n"
"	border-top-right-radius: none; \n"
"	border-top: none;\n"
"}")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.optionsPushButton = QPushButton(self.topFrame)
        self.optionsPushButton.setObjectName(u"optionsPushButton")
        self.optionsPushButton.setGeometry(QRect(20, 0, 30, 30))
        self.optionsPushButton.setMinimumSize(QSize(0, 0))
        self.optionsPushButton.setFont(font1)
        self.optionsPushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.optionsPushButton.setLayoutDirection(Qt.LeftToRight)
        self.optionsPushButton.setStyleSheet(u"QPushButton {\n"
"	border-image: url(images/optionsButton.svg) center;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"	border-image: url(images/optionsButtonHover.svg) center;\n"
"}")
        self.optionsPushButton.setCheckable(True)
        self.optionsPushButton.setFlat(False)
        self.exportPushButton = QPushButton(self.topFrame)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setGeometry(QRect(60, 0, 30, 30))
        self.exportPushButton.setMinimumSize(QSize(0, 0))
        self.exportPushButton.setFont(font1)
        self.exportPushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.exportPushButton.setLayoutDirection(Qt.LeftToRight)
        self.exportPushButton.setStyleSheet(u"QPushButton {\n"
"	border-image: url(images/exportButton.svg) center;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"	border-image: url(images/exportButtonHover.svg) center;\n"
"}")
        self.exportPushButton.setCheckable(True)
        self.exportPushButton.setFlat(False)
        self.presetComboBox = QComboBox(self.topFrame)
        self.presetComboBox.addItem("")
        self.presetComboBox.addItem("")
        self.presetComboBox.addItem("")
        self.presetComboBox.addItem("")
        self.presetComboBox.addItem("")
        self.presetComboBox.setObjectName(u"presetComboBox")
        self.presetComboBox.setGeometry(QRect(120, 0, 161, 30))
        self.presetComboBox.setLayoutDirection(Qt.LeftToRight)
        self.presetComboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: #E2E2E2;\n"
"	border-bottom-right-radius: 10px; \n"
"	color: #666666;\n"
"	padding: 1px 10px 1px 50px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"	background-color: #D3DDE0;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover {\n"
"	color: rgb(0, 159, 168);\n"
"}\n"
"\n"
"QComboBox QAbstractView {\n"
"	\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	background-color: rgb(237, 237, 237);\n"
"	padding: 5px;\n"
"	color: #666666;\n"
"	outline: none;\n"
"}\n"
"\n"
"QComboBox QListView::item {\n"
"	background-color: rgb(237, 237, 237);\n"
"	color: #666666;\n"
"	padding-left: 5px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
"	background-color: #D3DDE0;\n"
"	color: rgb(0, 159, 168);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	width: 30px;\n"
"	height: 30px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(images/dropDown.svg) center;\n"
"	width: 32px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover "
                        "{\n"
"	border-image: url(images/dropDownHover.svg) center;\n"
"}")
        self.presetComboBox.setFrame(True)
        self.presetPushButton = QPushButton(self.topFrame)
        self.presetPushButton.setObjectName(u"presetPushButton")
        self.presetPushButton.setGeometry(QRect(100, 0, 30, 30))
        self.presetPushButton.setMinimumSize(QSize(0, 0))
        self.presetPushButton.setFont(font1)
        self.presetPushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.presetPushButton.setLayoutDirection(Qt.LeftToRight)
        self.presetPushButton.setStyleSheet(u"QPushButton {\n"
"	border-image: url(images/presetButton.svg) center;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"	border-image: url(images/presetButtonHover.svg) center;\n"
"}")
        self.presetPushButton.setCheckable(True)
        self.presetPushButton.setFlat(False)
        self.presetComboBox.raise_()
        self.optionsPushButton.raise_()
        self.exportPushButton.raise_()
        self.presetPushButton.raise_()
        self.backgroundBottomFrameLabel = QLabel(self.centralwidget)
        self.backgroundBottomFrameLabel.setObjectName(u"backgroundBottomFrameLabel")
        self.backgroundBottomFrameLabel.setGeometry(QRect(140, 550, 181, 21))
        self.backgroundBottomFrameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: #E2E2E2;\n"
"	border-radius: 10px;\n"
"}")
        self.saveSendFrame = QFrame(self.centralwidget)
        self.saveSendFrame.setObjectName(u"saveSendFrame")
        self.saveSendFrame.setGeometry(QRect(250, 40, 60, 115))
        self.saveSendFrame.setFrameShape(QFrame.StyledPanel)
        self.saveSendFrame.setFrameShadow(QFrame.Raised)
        self.savePushButton = QPushButton(self.saveSendFrame)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(10, 65, 40, 40))
        self.savePushButton.setMinimumSize(QSize(0, 0))
        self.savePushButton.setFont(font2)
        self.savePushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.savePushButton.setLayoutDirection(Qt.LeftToRight)
        self.savePushButton.setStyleSheet(u"QPushButton {\n"
"	border-image: url(images/saveButton.svg) center;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"	border-image: url(images/saveButtonHover.svg) center;\n"
"}")
        self.savePushButton.setCheckable(True)
        self.savePushButton.setFlat(False)
        self.sendPushButton = QPushButton(self.saveSendFrame)
        self.sendPushButton.setObjectName(u"sendPushButton")
        self.sendPushButton.setGeometry(QRect(10, 10, 40, 40))
        self.sendPushButton.setMinimumSize(QSize(0, 0))
        self.sendPushButton.setFont(font1)
        self.sendPushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.sendPushButton.setLayoutDirection(Qt.LeftToRight)
        self.sendPushButton.setStyleSheet(u"QPushButton {\n"
"	border-image: url(images/sendButton.svg) center;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"	border-image: url(images/sendButtonHover.svg) center;\n"
"}")
        self.sendPushButton.setIconSize(QSize(20, 20))
        self.sendPushButton.setCheckable(True)
        self.sendPushButton.setFlat(False)
        self.backgroundTempGraphLabel = QLabel(self.centralwidget)
        self.backgroundTempGraphLabel.setObjectName(u"backgroundTempGraphLabel")
        self.backgroundTempGraphLabel.setGeometry(QRect(140, 420, 181, 121))
        self.backgroundTempGraphLabel.setStyleSheet(u"QLabel {\n"
"	background-color: #E2E2E2;\n"
"	border-radius: 15px;\n"
"}")
        self.currentFrame = QFrame(self.centralwidget)
        self.currentFrame.setObjectName(u"currentFrame")
        self.currentFrame.setEnabled(True)
        self.currentFrame.setGeometry(QRect(30, 165, 270, 70))
        self.currentFrame.setFont(font1)
        self.currentFrame.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #EDEDED;\n"
"	background-color: #EDEDED;\n"
"	color: #666666;\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #009FA8;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #D3DDE0;\n"
"}")
        self.currentFrame.setFrameShape(QFrame.StyledPanel)
        self.currentFrame.setFrameShadow(QFrame.Raised)
        self.currentSlider = QSlider(self.currentFrame)
        self.currentSlider.setObjectName(u"currentSlider")
        self.currentSlider.setGeometry(QRect(30, 10, 205, 22))
        self.currentSlider.setFont(font2)
        self.currentSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 6px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"	border-radius: 3px;\n"
"	margin-left: 1px;\n"
"	margin-right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #009FA8;\n"
"	width: 12px;\n"
"	margin: -4px -1px;\n"
"    border-radius: 7px;\n"
"	border: 1px solid #009FA8;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #009FA8;\n"
"	border-color: #181199;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background: qlineargradient(x1:1, y1:0.5, x2:0, y2:0.5, stop:0 #009FA8, stop:1 #181199);\n"
"	border-radius: 3px;\n"
"}")
        self.currentSlider.setMinimum(10)
        self.currentSlider.setMaximum(1900)
        self.currentSlider.setSingleStep(1)
        self.currentSlider.setValue(70)
        self.currentSlider.setSliderPosition(70)
        self.currentSlider.setOrientation(Qt.Horizontal)
        self.currentSlider.setTickPosition(QSlider.NoTicks)
        self.currentMinusFivePushButton = QPushButton(self.currentFrame)
        self.currentMinusFivePushButton.setObjectName(u"currentMinusFivePushButton")
        self.currentMinusFivePushButton.setGeometry(QRect(30, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.currentMinusFivePushButton.sizePolicy().hasHeightForWidth())
        self.currentMinusFivePushButton.setSizePolicy(sizePolicy1)
        self.currentMinusFivePushButton.setFont(font3)
        self.currentMinusFivePushButton.setStyleSheet(u"")
        self.currentMinusOnePushButton = QPushButton(self.currentFrame)
        self.currentMinusOnePushButton.setObjectName(u"currentMinusOnePushButton")
        self.currentMinusOnePushButton.setGeometry(QRect(90, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.currentMinusOnePushButton.sizePolicy().hasHeightForWidth())
        self.currentMinusOnePushButton.setSizePolicy(sizePolicy1)
        self.currentMinusOnePushButton.setFont(font3)
        self.currentMinusOnePushButton.setStyleSheet(u"")
        self.currentPlusFivePushButton = QPushButton(self.currentFrame)
        self.currentPlusFivePushButton.setObjectName(u"currentPlusFivePushButton")
        self.currentPlusFivePushButton.setGeometry(QRect(205, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.currentPlusFivePushButton.sizePolicy().hasHeightForWidth())
        self.currentPlusFivePushButton.setSizePolicy(sizePolicy1)
        self.currentPlusFivePushButton.setFont(font3)
        self.currentPlusFivePushButton.setStyleSheet(u"")
        self.currentPlusOnePushButton = QPushButton(self.currentFrame)
        self.currentPlusOnePushButton.setObjectName(u"currentPlusOnePushButton")
        self.currentPlusOnePushButton.setGeometry(QRect(147, 40, 30, 20))
        sizePolicy1.setHeightForWidth(self.currentPlusOnePushButton.sizePolicy().hasHeightForWidth())
        self.currentPlusOnePushButton.setSizePolicy(sizePolicy1)
        self.currentPlusOnePushButton.setFont(font3)
        self.currentPlusOnePushButton.setStyleSheet(u"")
        self.currentMaxLabel = QLabel(self.currentFrame)
        self.currentMaxLabel.setObjectName(u"currentMaxLabel")
        self.currentMaxLabel.setGeometry(QRect(248, 11, 21, 16))
        self.currentMaxLabel.setFont(font2)
        self.currentMinLabel = QLabel(self.currentFrame)
        self.currentMinLabel.setObjectName(u"currentMinLabel")
        self.currentMinLabel.setGeometry(QRect(12, 11, 16, 16))
        self.currentMinLabel.setFont(font2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.backgroundTempGraphLabel.raise_()
        self.backgroundBottomFrameLabel.raise_()
        self.topFrame.raise_()
        self.backgroundSliderLabel.raise_()
        self.backgroundCurrentDurationFrequencyLabel.raise_()
        self.currentDurationFrequencyFrame.raise_()
        self.startStopFrame.raise_()
        self.parametersFrame.raise_()
        self.tecFrame.raise_()
        self.tempGraphFrame.raise_()
        self.bottomFrame.raise_()
        self.saveSendFrame.raise_()
        self.durationFrame.raise_()
        self.frequencyFrame.raise_()
        self.currentFrame.raise_()

        self.retranslateUi(mainWindow)
        self.frequencySlider.valueChanged.connect(self.frequencyValueSpinBox.setValue)
        self.frequencyValueSpinBox.valueChanged.connect(self.frequencySlider.setValue)
        self.durationSlider.valueChanged.connect(self.durationValueSpinBox.setValue)
        self.durationValueSpinBox.valueChanged.connect(self.durationSlider.setValue)
        self.currentRadioButton.pressed.connect(self.currentFrame.show)
        self.currentRadioButton.pressed.connect(self.durationFrame.hide)
        self.durationRadioButton.pressed.connect(self.durationFrame.show)
        self.durationRadioButton.pressed.connect(self.currentFrame.hide)
        self.frequencyRadioButton.pressed.connect(self.frequencyFrame.show)
        self.frequencyRadioButton.pressed.connect(self.currentFrame.hide)
        self.frequencyRadioButton.pressed.connect(self.durationFrame.hide)
        self.durationRadioButton.pressed.connect(self.frequencyFrame.hide)
        self.currentRadioButton.pressed.connect(self.frequencyFrame.hide)
        self.currentRadioButton.pressed.connect(self.currentLineLabel.hide)
        self.durationRadioButton.clicked.connect(self.currentLineLabel.show)
        self.frequencyRadioButton.clicked.connect(self.currentLineLabel.show)
        self.durationRadioButton.pressed.connect(self.durationLineLabel.hide)
        self.currentRadioButton.clicked.connect(self.durationLineLabel.show)
        self.frequencyRadioButton.clicked.connect(self.durationLineLabel.show)
        self.frequencyRadioButton.pressed.connect(self.frequencyLineLabel.hide)
        self.currentRadioButton.clicked.connect(self.frequencyLineLabel.show)
        self.durationRadioButton.clicked.connect(self.frequencyLineLabel.show)

        self.presetComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.durationMinusTenPushButton.setText(QCoreApplication.translate("mainWindow", u"-10", None))
        self.durationPlusTwentyPushButton.setText(QCoreApplication.translate("mainWindow", u"+20", None))
        self.durationMinusTwentyPushButton.setText(QCoreApplication.translate("mainWindow", u"-20", None))
        self.durationMaxLabel.setText(QCoreApplication.translate("mainWindow", u"600", None))
        self.durationPlusTenPushButton.setText(QCoreApplication.translate("mainWindow", u"+10", None))
        self.durationMinLabel.setText(QCoreApplication.translate("mainWindow", u"20", None))
        self.durationRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c, \u043c\u043a\u0441", None))
        self.currentRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0422\u043e\u043a \u041d\u0430\u043a\u0430\u0447\u043a\u0438, \u0410", None))
        self.frequencyRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430, \u0413\u0446", None))
        self.durationLineLabel.setText("")
        self.frequencyLineLabel.setText("")
        self.currentLineLabel.setText("")
        self.stopRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0422\u041e\u041f", None))
        self.startRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0422\u0410\u0420\u0422", None))
        self.backgroudStartStopLabel.setText("")
        self.externalTriggerRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0412\u041d\u0415\u0428\u041d\u0418\u0419\n"
"  \u0417\u0410\u041f\u0423\u0421\u041a", None))
        self.backgroundCurrentDurationFrequencyLabel.setText("")
        self.backgroundSliderLabel.setText("")
        self.frequencyMaxLabel.setText(QCoreApplication.translate("mainWindow", u"50", None))
        self.frequencyMinLabel.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.frequencyPlusOnePushButton.setText(QCoreApplication.translate("mainWindow", u"+1", None))
        self.frequencyPlusFivePushButton.setText(QCoreApplication.translate("mainWindow", u"+5", None))
        self.frequencyMinusOnePushButton.setText(QCoreApplication.translate("mainWindow", u"-1", None))
        self.frequencyMinusFivePushButton.setText(QCoreApplication.translate("mainWindow", u"-5", None))
        self.parametersLineLabel.setText("")
        self.factDurationValueLabel.setText(QCoreApplication.translate("mainWindow", u"2256", None))
        self.offFDPumpingCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u043a\u043b. \u043d\u0430\u043a\u0430\u0447\u043a\u0438 \u043f\u043e \u0424\u0414", None))
        self.voltageLabel.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435, \u0412", None))
        self.PCDCheckBox.setText(QCoreApplication.translate("mainWindow", u"PCD-21", None))
        self.jitterStabCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0431. \u0434\u0436\u0438\u0442\u0442\u0435\u0440\u0430", None))
        self.randefinderValueLabel.setText(QCoreApplication.translate("mainWindow", u"50250", None))
        self.randefinderLabel.setText(QCoreApplication.translate("mainWindow", u"\u0414\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c, \u043c", None))
        self.rangefinderCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0414\u0430\u043b\u044c\u043d\u043e\u043c\u0435\u0440", None))
        self.factDurationLabel.setText(QCoreApplication.translate("mainWindow", u"\u0424\u0430\u043a\u0442. \u0434\u043b\u0438\u0442\u0435\u043b., \u043c\u043a\u0441", None))
        self.delayLabel.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430, \u043c\u043a\u0441", None))
        self.PWMLabel.setText(QCoreApplication.translate("mainWindow", u"\u0428\u0418\u041c, %", None))
        self.stabTempRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0431\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.offTempRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043e", None))
        self.rangeTempRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d", None))
        self.tecLabel.setText(QCoreApplication.translate("mainWindow", u"\u0422\u042d\u041a", None))
        self.stabTempDegreesLabel.setText(QCoreApplication.translate("mainWindow", u"\u00b0\u0421", None))
        self.rangeTempHyphenLabel.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.rangeTempDegreesLabel.setText(QCoreApplication.translate("mainWindow", u"\u00b0\u0421", None))
        self.tempGraphDegreesLabel.setText(QCoreApplication.translate("mainWindow", u"\u00b0\u0421", None))
        self.tempGraphValueLabel.setText(QCoreApplication.translate("mainWindow", u"25.3", None))
        self.tempGraphPlusPushButton.setText(QCoreApplication.translate("mainWindow", u"+", None))
        self.tempGraphMinusPushButton.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.powerSupplyNumberLabel.setText(QCoreApplication.translate("mainWindow", u"\u0411\u043b\u043e\u043a \u21160001", None))
        self.connectIconLabel.setText("")
        self.disconnectIconLabel.setText("")
        self.optionsPushButton.setText("")
        self.exportPushButton.setText("")
        self.presetComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u041b\u0414\u0426", None))
        self.presetComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u041c\u041e\u041e\u041f\u0421", None))
        self.presetComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u041b\u0418\u0414\u041f", None))
        self.presetComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"\u041b-60", None))
        self.presetComboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"\u041b-130", None))

        self.presetPushButton.setText("")
        self.backgroundBottomFrameLabel.setText("")
        self.savePushButton.setText("")
        self.sendPushButton.setText("")
        self.backgroundTempGraphLabel.setText("")
        self.currentMinusFivePushButton.setText(QCoreApplication.translate("mainWindow", u"-5", None))
        self.currentMinusOnePushButton.setText(QCoreApplication.translate("mainWindow", u"-1", None))
        self.currentPlusFivePushButton.setText(QCoreApplication.translate("mainWindow", u"+5", None))
        self.currentPlusOnePushButton.setText(QCoreApplication.translate("mainWindow", u"+1", None))
        self.currentMaxLabel.setText(QCoreApplication.translate("mainWindow", u"230", None))
        self.currentMinLabel.setText(QCoreApplication.translate("mainWindow", u"0", None))
    # retranslateUi

