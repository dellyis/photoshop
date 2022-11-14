import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class Photoshop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.default_stylesheet = {}
        self.total_filter_page = 2
        self.filter_page = 0
        self.load_ui()

    def load_ui(self):
        self.new_name.textChanged.connect(self.placeholder_style_editor)
        self.placeholder_style_editor(self.new_name)

        self.img_link.textChanged.connect(self.placeholder_style_editor)
        self.placeholder_style_editor(self.img_link)

        for i in range(self.total_filter_page):
            eval(f"self.filter_page_{i}").hide()
        eval(f"self.filter_page_{self.filter_page}").show()

        self.filters_nav_first.clicked.connect(lambda: self.edit_filter_page(-self.filter_page))
        self.filters_nav_prev.clicked.connect(lambda: self.edit_filter_page(-1))
        self.filters_nav_next.clicked.connect(lambda: self.edit_filter_page(1))
        self.filters_nav_last.clicked.connect(lambda: self.edit_filter_page(self.total_filter_page - 1))

        self.filters_nav_first.setDisabled(self.filter_page == 0)
        self.filters_nav_prev.setDisabled(self.filter_page == 0)
        self.filters_nav_next.setDisabled(self.filter_page == self.total_filter_page - 1)
        self.filters_nav_last.setDisabled(self.filter_page == self.total_filter_page - 1)

        self.filters_page.setText(f"{self.filter_page + 1}/{self.total_filter_page}")

        # self.img_link_2.textChanged.connect(self.placeholder_style_editor)
        # self.placeholder_style_editor(self.img_link_2)

        # self.scrollArea.setWidget(self.verticalLayout_2)
        # self.scrollArea.setWidgetResizable(True)
        # self.img_dl_2.hide()
        # self.groupBox.hide()

    def placeholder_style_editor(self, el=None):
        parent = self.sender() or el
        if self.default_stylesheet.get(parent.objectName()) is None:
            self.default_stylesheet[parent.objectName()] = parent.styleSheet()
        if parent.text() == "":
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()] + "\n\n" + f"{type(parent)}"[24:-2]
                                 + " {\n  color: rgba(255, 255, 255, 75);\n}")
        else:
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()])

    def edit_filter_page(self, count):
        if self.filter_page + count not in range(self.total_filter_page):
            return
        eval(f"self.filter_page_{self.filter_page}").hide()
        self.filter_page += count
        self.filters_nav_first.setDisabled(self.filter_page == 0)
        self.filters_nav_prev.setDisabled(self.filter_page == 0)
        self.filters_nav_next.setDisabled(self.filter_page == self.total_filter_page - 1)
        self.filters_nav_last.setDisabled(self.filter_page == self.total_filter_page - 1)
        eval(f"self.filter_page_{self.filter_page}").show()
        self.filters_page.setText(f"{self.filter_page + 1}/{self.total_filter_page}")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Photoshop()
    ex.show()
    sys.exit(app.exec_())
