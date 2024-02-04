from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QPointF, QRectF


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("Temperature Chart")

        series = QLineSeries()

        # series.append(0, 6)
        # series.append(2, 5)
        # series.append(4, 8)
        # series.append(6, 10)
        # series.append(8, 8)

        series << QPointF(11.1, 1) << QPointF(13, 3) << QPointF(17, 6) \
               << QPointF(18, 3) << QPointF(20, 2)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart")
        chart.setBackgroundVisible(False)
        chart.setPlotArea(QRectF(0, 0, 200, 100))
        chart.legend().hide()
        chart.zoom(1.2)

        chartview = QChartView(chart)
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
