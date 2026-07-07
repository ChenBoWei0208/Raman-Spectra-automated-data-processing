# This Python file uses the following encoding: utf-8
import sys
# 1. 統一全部從 PySide6 匯入（不要混用 PyQt6）
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
import pyqtgraph as pg
# Important:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import pyqtgraph.exporters as exporters
from scipy.signal import savgol_filter
import random


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.chart = pg.PlotWidget()


    def update_chart(self, is_filter = False):
        if is_filter:
            width = 3
        else :
            width = 1
        current_mode = self.ui.stack_box.currentText()
        random_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        if current_mode == "stack chart":
            self.chart.plot(self.x_data, self.y_data, pen=pg.mkPen(random_color, width=width))
        elif current_mode == "non-stack chart":
            self.chart.clear()
            self.chart.plot(self.x_data, self.y_data)

    @Slot()
    def on_Open_File_clicked(self):
        filePath, filterType = QFileDialog.getOpenFileName(filter='TXT(*.txt)')
        if filePath:
            self.ui.layout.addWidget(self.chart)
            try:
                self.x_data = []
                self.y_data = []
                with open(filePath,'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line: continue
                        parts = line.split('\t')
                        x = float(parts[0].strip())
                        y = float(parts[1].strip())
                        self.x_data.append(x)
                        self.y_data.append(y)
                    self.update_chart()
                    self.ui.textEdit.setPlainText(f"successful open: {filePath}")
            except Exception as e:
               self.ui.textEdit.setPlainText(f"fail open: {e}")


    @Slot()
    def on_filterButton_clicked(self):
        self.y_data = savgol_filter(self.y_data, window_length=31, polyorder=3)
        self.update_chart(is_filter = True)
        self.ui.textEdit.setPlainText("successful filter")

    @Slot()
    def on_Save_File_clicked(self):
        filePath, filterType = QFileDialog.getSaveFileName(filter='PNG(*.png)')
        if filePath:
            try:
                    exporter = exporters.ImageExporter(self.chart.plotItem)
                    exporter.export(filePath)
                    self.ui.textEdit.setPlainText(f"successful save: {filePath}")
            except Exception as e:
                self.ui.textEdit.setPlainText(f"failure save: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
