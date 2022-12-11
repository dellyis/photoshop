import logging
import os
import shutil
import sys
import sqlite3 as sql

import PIL
import requests
from PIL import Image
from PyQt5 import uic  # type: ignore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog

import design
from filters import Filters

logging.basicConfig(level=logging.INFO, filename=".log", filemode="a",
                    format="%(asctime)s %(name)-30s %(levelname)-8s %(message)s")
log = logging.getLogger("application")

FILTERS = Filters()
ACTIVE_FILTERS = ["black_white", "negative", "inversion_red", "inversion_green", "inversion_blue", "black_gray_white",
                  "retro", "neon_retro", "sakura", "total_black_white", "white_balance", "black_balance"]

db = sql.connect("presets.db")
cursor = db.cursor()


class CreatePreset(QDialog, design.PresetDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.res = False

        self.name.textChanged.connect(self.enable_create)
        [eval("self." + i, {"self": self}).stateChanged.connect(self.enable_create) for i in ACTIVE_FILTERS]
        self.create.clicked.connect(self.create_preset)  # type: ignore

    def enable_create(self):
        self.create.setDisabled(not (self.name.text().strip() and self.any_filters()))  # type: ignore

    def any_filters(self):
        return any(map(lambda el: eval("self." + el + ".isChecked()", {"self": self}), ACTIVE_FILTERS))

    def create_preset(self):
        selected = filter(lambda el: eval("self." + el + ".isChecked()", {"self": self}), ACTIVE_FILTERS)
        db_filter = 0
        for i in selected:
            db_filter += 1 << cursor.execute("SELECT id FROM filters WHERE name=?", (i, )).fetchall()[0][0]
        cursor.execute("INSERT INTO presets(name,filters) VALUES(?,?)", (self.name.text().strip(), db_filter))
        db.commit()
        self.res = True
        self.close()


class Photoshop(QMainWindow, design.Window):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        # uic.loadUi('main.ui', self)
        self.saved = True
        self.image = None
        self.pixels = None
        self.filepath = None
        self.default_stylesheet = {}
        self.total_filter_page = 2
        self.filter_page = 0
        self.load_ui()

    def load_ui(self):
        """
        Подключение всего дизайна
        """
        [eval(f"self.{i}").clicked.connect(self.filter) for i in ACTIVE_FILTERS]
        self.open.clicked.connect(lambda: self.open_img(True))
        self.close.clicked.connect(self.close_img)

        self.create_preset.clicked.connect(self.open_create_preset)

        self.save.clicked.connect(self.func_save_file)
        self.save_as.clicked.connect(self.save_as_file)

        self.img_dl.clicked.connect(lambda: self.open_img(False))

        self.img_dl.setDisabled(True)
        self.img_link.textChanged.connect(self.placeholder_style_editor)
        self.img_link.textChanged.connect(self.unlock_img_dl)
        self.placeholder_style_editor(self.img_link)

        for i in range(self.total_filter_page):
            eval(f"self.filter_page_{i}").hide()
        eval(f"self.filter_page_{self.filter_page}").show()

        self.filters_nav_first.clicked.connect(lambda: self.edit_filter_page(-self.filter_page))
        self.filters_nav_prev.clicked.connect(lambda: self.edit_filter_page(-1))
        self.filters_nav_next.clicked.connect(lambda: self.edit_filter_page(1))
        self.filters_nav_last.clicked.connect(
            lambda: self.edit_filter_page(self.total_filter_page - self.filter_page - 1))

        self.toggle_filter_navigation()
        self.filters_page.setText(f"{self.filter_page + 1}/{self.total_filter_page}")

        self.channel_togglers.hide()

        self.channels_reset.setDisabled(True)
        self.channels_reset.clicked.connect(self.reset)

        self.channels_commit.setDisabled(True)
        self.channels_commit.clicked.connect(self.commit)

        self.load_presets()

        self.commit_preset.clicked.connect(self.preset_commit)

        [i.valueChanged.connect(self.channel_increase) for i in (self.red_slider, self.green_slider, self.blue_slider)]

    def open_create_preset(self):
        create_preset = CreatePreset()

        create_preset.name.textChanged.connect(self.placeholder_style_editor)

        create_preset.open()
        create_preset.exec_()

        if create_preset.res:
            self.load_presets()

    def load_presets(self):
        self.preset_box.clear()

        presets = cursor.execute("SELECT * FROM presets").fetchall()

        for preset in presets:
            self.preset_box.addItem(preset[1])

    def preset_commit(self):
        need_filter = self.preset_box.itemText(0)
        data = cursor.execute("SELECT filters FROM presets WHERE name=?", (need_filter, )).fetchall()[0][0]
        filters_data = cursor.execute("SELECT * FROM filters").fetchall()
        for i in filters_data:
            print(i)
            if data & 1 << i[0]:
                self.filter(i[1], i[2])

    def closeEvent(self, event):
        """
        Замена стандартного события закрытия программы на подтверждение
        """
        if not os.path.exists("cache"):
            return
        close = QMessageBox()
        close.setText("У вас открыто изображение!\nЗавершить работу?\nНесохранённые изменения будут потеряны!")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            shutil.rmtree("cache")
            log.info("Program has been closed")
            event.accept()
        else:
            event.ignore()

    def placeholder_style_editor(self, el=None):
        """
        Изменение стилей для заменителей в QLineEdit
        """
        parent = self.sender() or el
        if self.default_stylesheet.get(parent.objectName()) is None:
            self.default_stylesheet[parent.objectName()] = parent.styleSheet()
        if parent.text() == "":
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()] + "\n\n" + f"{type(parent)}"[24:-2]
                                 + " {\n  color: rgba(255, 255, 255, 75);\n}")
        else:
            parent.setStyleSheet(self.default_stylesheet[parent.objectName()])

    def edit_filter_page(self, count):
        """
        Перелистывание страниц с фильтрами
        """
        if self.filter_page + count not in range(self.total_filter_page):
            return
        eval(f"self.filter_page_{self.filter_page}").hide()
        self.filter_page += count
        self.toggle_filter_navigation()
        eval(f"self.filter_page_{self.filter_page}").show()
        self.filters_page.setText(f"{self.filter_page + 1}/{self.total_filter_page}")

    def toggle_filter_navigation(self):
        """
        Включение/отключение кнопок навигации по фильтрам
        """
        self.filters_nav_first.setDisabled(self.filter_page == 0)
        self.filters_nav_prev.setDisabled(self.filter_page == 0)
        self.filters_nav_next.setDisabled(self.filter_page == self.total_filter_page - 1)
        self.filters_nav_last.setDisabled(self.filter_page == self.total_filter_page - 1)

    def unlock_img_dl(self):
        """
        Включение кнопки загрузки изображения, когда введена ссылка
        """
        self.img_dl.setDisabled(not bool(self.sender().text()))  # type: ignore

    def open_img(self, local=True):
        """
        Загрузка и открытие изображения
        """
        result = False
        if local:
            self.filepath = QFileDialog.getOpenFileName(self, "Выбрать картинку", filter="Картинка (*.jpg *.png);;Все "
                                                                                         "файлы (*)")[0]
            if self.filepath:
                log.info("Image path: " + self.filepath)
                if not os.path.exists("cache"):
                    os.mkdir("cache")
                Image.open(self.filepath).resize((580, 580)).save("cache/original.png")
                self.log.setText("Картинка открыта")
                result = True
        else:
            self.filepath = None
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка загрузки картинки")
            try:
                log.info("Image url: " + self.img_link.text())
                request_result = requests.get(self.img_link.text(), stream=True).raw
                if not os.path.exists("cache"):
                    os.mkdir("cache")
                Image.open(request_result).resize((580, 580)).save("cache/original.png")
                log.info("Image has been downloaded")
                self.log.setText("Картинка загружена и открыта")
                result = True
            except requests.exceptions.MissingSchema:
                msg.setText("В ссылке отсутствует протокол (http(s)://)")
                msg.exec_()
            except requests.exceptions.InvalidSchema:
                msg.setText("Недопустимый протокол (доступные: http(s)://)")
                msg.exec_()
            except requests.exceptions.ConnectionError:
                msg.setText("Недостижимый хост\nВозможно, отсутствует подключение к интернету.")
                msg.exec_()
            except requests.exceptions.Timeout:
                msg.setText("Получение картинки заняло слишком много времени")
                msg.exec_()
            except PIL.UnidentifiedImageError:
                msg.setText("Ссылка ведёт не на изображение")
                msg.exec_()
            except Exception as e:
                log.exception(e)
        if result:
            self.img.setPixmap(QPixmap("cache/original.png"))
            self.image = Image.open("cache/original.png")
            self.pixels = self.image.load()
            self.toggle_btns(True)
            self.img_link.setText("")
            if not local:
                self.save.setDisabled(True)

    def close_img(self):
        """
        Закрытие изображения
        """
        self.img.setPixmap(QPixmap())
        self.image = None
        self.pixels = None
        self.log.setText("")
        shutil.rmtree("cache")
        self.filepath = None
        self.toggle_btns(False)
        log.info("Image has been closed")

    def toggle_btns(self, toggle):
        """
        Переключение активности кнопок изменения изображения
        """
        [eval("self." + el, {"self": self}).setDisabled(toggle) for el in ("open", "img_link")]
        [eval("self." + el, {"self": self}).setDisabled(not toggle) for el in (("close", "save", "save_as", "channels",
                                                                                "channel_togglers", "preset_box",
                                                                                "commit_preset") +
                                                                               tuple(f"filter_page_{i}" for i in
                                                                                     range(self.total_filter_page)))]
        [eval("self." + el + "_toggler", {"self": self}).setChecked(toggle) for el in ("red", "green", "blue")]
        [eval("self." + el + "_slider", {"self": self}).setValue(0) for el in ("red", "green", "blue")]

    def filter(self, name=None, display_name=None):
        """
        Обработка нажатия на кнопки фильтров
        """
        if not name:
            sender = self.sender()
            name = sender.text()  # type: ignore
            function = FILTERS[sender.objectName()]
        else:
            function = FILTERS[name]
        x, y = self.image.size
        for i in range(x):
            for j in range(y):
                self.pixels[i, j] = function(*self.pixels[i, j])
        self.image.save("cache/original.png")
        self.img.setPixmap(QPixmap("cache/original.png"))
        self.log.setText(f"Применён фильтр \"{display_name or name}\"")
        log.info(f"\"{name}\" filter apllied")

    def channel_increase(self):
        """
        Увеличить интенсивность канала
        """
        add_r = self.red_slider.value()
        add_g = self.green_slider.value()
        add_b = self.blue_slider.value()
        image = Image.open("cache/original.png")
        x, y = image.size
        pixels = image.load()
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]  # type: ignore
                pixels[i, j] = min(255, r + add_r), min(255, g + add_g), min(255, b + add_b)  # type: ignore
        self.channels_reset.setDisabled(False)
        self.channels_commit.setDisabled(False)
        image.save("cache/not_commited.png")
        self.img.setPixmap(QPixmap("cache/not_commited.png"))

    def reset(self):
        self.red_slider.setValue(0)
        self.green_slider.setValue(0)
        self.blue_slider.setValue(0)
        os.remove("cache/not_commited.png")
        self.img.setPixmap(QPixmap("cache/original.png"))
        self.channels_reset.setDisabled(True)
        self.channels_commit.setDisabled(True)

    def commit(self):
        os.replace("cache/not_commited.png", "cache/original.png")
        self.img.setPixmap(QPixmap("cache/original.png"))
        self.red_slider.setValue(0)
        self.green_slider.setValue(0)
        self.blue_slider.setValue(0)
        self.channels_reset.setDisabled(True)
        self.channels_commit.setDisabled(True)

    def func_save_file(self):
        self.image.save(self.filepath)
        self.log.setText("Изображение сохранено")
        log.info("Image has been saved")

    def save_as_file(self):
        res = QFileDialog.getSaveFileName(self, "Сохранить изображение", filter='.png')[0]
        if res:
            self.image.save(res.rstrip(".png") + ".png")
            self.log.setText("Изображение сохранено")
            log.info("Image has been saved")
            self.filepath = res.rstrip(".png") + ".png"


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Photoshop()
    ex.show()
    sys.exit(app.exec_())
