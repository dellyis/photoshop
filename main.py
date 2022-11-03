import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class Photoshop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.default_stylesheet = {}
        self.load_ui()

    def load_ui(self):
        self.new_name.textChanged.connect(self.placeholder_style_editor)
        self.placeholder_style_editor(self.new_name)

        self.img_link.textChanged.connect(self.placeholder_style_editor)
        self.placeholder_style_editor(self.img_link)

    def placeholder_style_editor(self, el=None):
        parent = self.sender() or el
        if self.default_stylesheet.get(parent.objectName()) is None:
            self.default_stylesheet[parent.objectName()] = parent.styleSheet()
        if parent.text() == "":
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()] + "\n\n" + f"{type(parent)}"[24:-2]
                                 + " {\n  color: rgba(255, 255, 255, 75);\n}")
        else:
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Photoshop()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
