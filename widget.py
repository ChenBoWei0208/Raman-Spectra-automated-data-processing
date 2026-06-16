# This Python file uses the following encoding: utf-8
import sys
# 1. 統一全部從 PySide6 匯入（不要混用 PyQt6）
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget

# Important:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    @Slot()
    def on_Open_File_clicked(self):
        filePath, filterType = QFileDialog.getOpenFileName(filter='TXT(*.txt)')
        if filePath:
            try:
                with open(filePath,'r', encoding='utf-8') as f:
                    text = f.read()
                    self.ui.view.setPlainText(str(text))
                    print(f"successful open:{filePath}")
            except Exception as e:
                print(f"fail open:{e}")
    @Slot()
    def on_Save_File_clicked(self):
        filePath, filterType = QFileDialog.getSaveFileName(filter='TXT(*.txt)')
        if filePath:
            try:
                with open(filePath,'w', encoding='utf-8') as f:
                    text = self.ui.view.toPlainText()
                    f.write(str(text))
                    print(f"successful save:{filePath}")
            except Exception as e:
                print(f"failure save{e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
