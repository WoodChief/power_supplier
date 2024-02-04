from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF


class TempGraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 200, 100)
        self.series = QLineSeries()
        self.chart = QChart()
        self.range_x = 100
        self.max_x = self.range_x
        self.range_y = 45
        self.max_y = self.range_y
        self.zoom_value = 1
        self.chart.setPlotArea(QRectF(0, 0, 200, 100))
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(QValueAxis(), self.series)
        self.chart.setAxisY(QValueAxis(), self.series)
        self.set_axis_range()
        self.chart.setBackgroundVisible(True)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().hide()

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.chartview)
        self.setLayout(self.vbox)
        self.position = 0

        # Connections #
        self.series.pointAdded.connect(
            self.on_new_point_added
        )

    def set_axis_range(self):
        self.chart.axisX().setRange(self.max_x - self.range_x,
                                    self.max_x)
        self.chart.axisY().setRange(self.max_y - self.range_y,
                                    self.max_y)

    def zoom(self, value):
        self.zoom_value = value
        self.range_x = self.range_x / self.zoom_value
        self.max_x = ((self.max_x - self.position)/self.zoom_value
                      + self.position)
        self.set_axis_range()

    def on_new_point_added(self):
        self.position += 1
        if self.position > self.max_x - self.range_x * 0.2:
            self.max_x += 1
            self.set_axis_range()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TempGraphWidget()
    main.show()
    sys.exit(app.exec())
