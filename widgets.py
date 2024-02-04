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
        self.min_x = 0
        self.max_x = 100
        self.min_y = 0
        self.max_y = 45
        self.chart.setPlotArea(QRectF(0, 0, 200, 100))
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(QValueAxis(), self.series)
        self.chart.setAxisY(QValueAxis(), self.series)
        self.chart.setBackgroundVisible(True)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().hide()

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.chartview)
        self.setLayout(self.vbox)
        self.tick_counter = 0

        # Connections #
        self.series.pointAdded.connect(
            self.on_new_point_added
        )

    def set_axis_range(self):
        self.chart.axisX().setRange(self.min_x, self.max_x)
        self.chart.axisY().setRange(self.min_y, self.max_y)

    def on_new_point_added(self):
        self.tick_counter += 1
        if self.tick_counter > 100:
            self.min_x += 1
            self.max_x += 1
            self.set_axis_range()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TempGraphWidget()
    main.show()
    sys.exit(app.exec())
