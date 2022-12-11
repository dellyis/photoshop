from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Window:
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(941, 632)
        Window.setMinimumSize(QSize(941, 632))
        Window.setMaximumSize(QSize(941, 632))
        Window.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 320, 580))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QWidget {\n"
"	selection-background-color: #5865F2;\n"
"	border-bottom-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.file_tab = QWidget()
        self.file_tab.setObjectName(u"file_tab")
        self.download_file = QFrame(self.file_tab)
        self.download_file.setObjectName(u"download_file")
        self.download_file.setEnabled(True)
        self.download_file.setGeometry(QRect(10, 310, 301, 131))
        self.download_file.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.download_file.setFrameShape(QFrame.StyledPanel)
        self.download_file.setFrameShadow(QFrame.Raised)
        self.img_link = QLineEdit(self.download_file)
        self.img_link.setObjectName(u"img_link")
        self.img_link.setEnabled(True)
        self.img_link.setGeometry(QRect(20, 20, 261, 41))
        self.img_link.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"	border: 1px solid #5865F2;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.img_dl = QPushButton(self.download_file)
        self.img_dl.setObjectName(u"img_dl")
        self.img_dl.setEnabled(True)
        self.img_dl.setGeometry(QRect(20, 70, 261, 41))
        self.img_dl.setCursor(QCursor(Qt.PointingHandCursor))
        self.img_dl.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.open_file = QFrame(self.file_tab)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setEnabled(True)
        self.open_file.setGeometry(QRect(10, 10, 301, 131))
        self.open_file.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.open_file.setFrameShape(QFrame.StyledPanel)
        self.open_file.setFrameShadow(QFrame.Raised)
        self.open = QPushButton(self.open_file)
        self.open.setObjectName(u"open")
        self.open.setGeometry(QRect(20, 20, 261, 41))
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        self.open.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.close = QPushButton(self.open_file)
        self.close.setObjectName(u"close")
        self.close.setEnabled(False)
        self.close.setGeometry(QRect(20, 70, 261, 41))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.save_file = QFrame(self.file_tab)
        self.save_file.setObjectName(u"save_file")
        self.save_file.setEnabled(True)
        self.save_file.setGeometry(QRect(10, 160, 301, 131))
        self.save_file.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.save_file.setFrameShape(QFrame.StyledPanel)
        self.save_file.setFrameShadow(QFrame.Raised)
        self.save = QPushButton(self.save_file)
        self.save.setObjectName(u"save")
        self.save.setEnabled(False)
        self.save.setGeometry(QRect(20, 20, 261, 41))
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        self.save.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.save_as = QPushButton(self.save_file)
        self.save_as.setObjectName(u"save_as")
        self.save_as.setEnabled(False)
        self.save_as.setGeometry(QRect(20, 70, 261, 41))
        self.save_as.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_as.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.tabWidget.addTab(self.file_tab, "")
        self.channels_tab = QWidget()
        self.channels_tab.setObjectName(u"channels_tab")
        self.channels = QFrame(self.channels_tab)
        self.channels.setObjectName(u"channels")
        self.channels.setEnabled(False)
        self.channels.setGeometry(QRect(10, 10, 301, 281))
        self.channels.setCursor(QCursor(Qt.ArrowCursor))
        self.channels.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.channels.setFrameShape(QFrame.StyledPanel)
        self.channels.setFrameShadow(QFrame.Raised)
        self.red_channel = QFrame(self.channels)
        self.red_channel.setObjectName(u"red_channel")
        self.red_channel.setGeometry(QRect(20, 70, 261, 41))
        self.red_channel.setAutoFillBackground(False)
        self.red_channel.setStyleSheet(u"QFrame {\n"
"	border: solid white;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.red_channel.setFrameShape(QFrame.StyledPanel)
        self.red_channel.setFrameShadow(QFrame.Raised)
        self.red_slider = QSlider(self.red_channel)
        self.red_slider.setObjectName(u"red_slider")
        self.red_slider.setGeometry(QRect(40, 10, 211, 20))
        self.red_slider.setCursor(QCursor(Qt.SizeHorCursor))
        self.red_slider.setStyleSheet(u"QSlider {\n"
"	border: none;\n"
"	selection-background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QSlider:handle:hover, QSlider:handle:focus {\n"
"    background: rgb(47, 47, 47);\n"
"    border: 1px solid rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.red_slider.setMaximum(255)
        self.red_slider.setSingleStep(5)
        self.red_slider.setOrientation(Qt.Horizontal)
        self.red_circle = QLabel(self.red_channel)
        self.red_circle.setObjectName(u"red_circle")
        self.red_circle.setGeometry(QRect(10, 10, 21, 21))
        self.red_circle.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"")
        self.green_channel = QFrame(self.channels)
        self.green_channel.setObjectName(u"green_channel")
        self.green_channel.setGeometry(QRect(20, 120, 261, 41))
        self.green_channel.setAutoFillBackground(False)
        self.green_channel.setStyleSheet(u"QFrame {\n"
"	border: solid white;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.green_channel.setFrameShape(QFrame.StyledPanel)
        self.green_channel.setFrameShadow(QFrame.Raised)
        self.green_slider = QSlider(self.green_channel)
        self.green_slider.setObjectName(u"green_slider")
        self.green_slider.setGeometry(QRect(40, 10, 211, 20))
        self.green_slider.setCursor(QCursor(Qt.SizeHorCursor))
        self.green_slider.setStyleSheet(u"QSlider {\n"
"	border: none;\n"
"	selection-background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QSlider:handle:hover, QSlider:handle:focus {\n"
"    background: rgb(47, 47, 47);\n"
"    border: 1px solid rgb(0, 255, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.green_slider.setMaximum(255)
        self.green_slider.setSingleStep(5)
        self.green_slider.setOrientation(Qt.Horizontal)
        self.green_circle = QLabel(self.green_channel)
        self.green_circle.setObjectName(u"green_circle")
        self.green_circle.setGeometry(QRect(10, 10, 21, 21))
        self.green_circle.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;\n"
"")
        self.blue_channel = QFrame(self.channels)
        self.blue_channel.setObjectName(u"blue_channel")
        self.blue_channel.setGeometry(QRect(20, 170, 261, 41))
        self.blue_channel.setAutoFillBackground(False)
        self.blue_channel.setStyleSheet(u"QFrame {\n"
"	border: solid white;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.blue_channel.setFrameShape(QFrame.StyledPanel)
        self.blue_channel.setFrameShadow(QFrame.Raised)
        self.blue_slider = QSlider(self.blue_channel)
        self.blue_slider.setObjectName(u"blue_slider")
        self.blue_slider.setGeometry(QRect(40, 10, 211, 20))
        self.blue_slider.setCursor(QCursor(Qt.SizeHorCursor))
        self.blue_slider.setStyleSheet(u"QSlider {\n"
"	border: none;\n"
"	selection-background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QSlider:handle:hover, QSlider:handle:focus {\n"
"    background: rgb(47, 47, 47);\n"
"    border: 1px solid rgb(0, 0, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.blue_slider.setMaximum(255)
        self.blue_slider.setSingleStep(5)
        self.blue_slider.setOrientation(Qt.Horizontal)
        self.blue_circle = QLabel(self.blue_channel)
        self.blue_circle.setObjectName(u"blue_circle")
        self.blue_circle.setGeometry(QRect(10, 10, 21, 21))
        self.blue_circle.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius: 10px;\n"
"")
        self.channels_reset = QPushButton(self.channels)
        self.channels_reset.setObjectName(u"channels_reset")
        self.channels_reset.setGeometry(QRect(20, 20, 261, 41))
        self.channels_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.channels_reset.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.channels_commit = QPushButton(self.channels)
        self.channels_commit.setObjectName(u"channels_commit")
        self.channels_commit.setGeometry(QRect(20, 220, 261, 41))
        self.channels_commit.setCursor(QCursor(Qt.PointingHandCursor))
        self.channels_commit.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.channel_togglers = QFrame(self.channels_tab)
        self.channel_togglers.setObjectName(u"channel_togglers")
        self.channel_togglers.setEnabled(False)
        self.channel_togglers.setGeometry(QRect(10, 300, 301, 231))
        self.channel_togglers.setCursor(QCursor(Qt.ArrowCursor))
        self.channel_togglers.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.channel_togglers.setFrameShape(QFrame.StyledPanel)
        self.channel_togglers.setFrameShadow(QFrame.Raised)
        self.green_toggler = QCheckBox(self.channel_togglers)
        self.green_toggler.setObjectName(u"green_toggler")
        self.green_toggler.setGeometry(QRect(20, 70, 261, 41))
        self.green_toggler.setCursor(QCursor(Qt.PointingHandCursor))
        self.green_toggler.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"	selection-background-color: #0f0;\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.blue_toggler = QCheckBox(self.channel_togglers)
        self.blue_toggler.setObjectName(u"blue_toggler")
        self.blue_toggler.setGeometry(QRect(20, 120, 261, 41))
        self.blue_toggler.setCursor(QCursor(Qt.PointingHandCursor))
        self.blue_toggler.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"	selection-background-color: #00f;\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.red_toggler = QCheckBox(self.channel_togglers)
        self.red_toggler.setObjectName(u"red_toggler")
        self.red_toggler.setGeometry(QRect(20, 20, 261, 41))
        self.red_toggler.setCursor(QCursor(Qt.PointingHandCursor))
        self.red_toggler.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"	selection-background-color: #f00;\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.togglers_commit = QPushButton(self.channel_togglers)
        self.togglers_commit.setObjectName(u"togglers_commit")
        self.togglers_commit.setGeometry(QRect(20, 170, 261, 41))
        self.togglers_commit.setCursor(QCursor(Qt.PointingHandCursor))
        self.togglers_commit.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.tabWidget.addTab(self.channels_tab, "")
        self.filters_tab = QWidget()
        self.filters_tab.setObjectName(u"filters_tab")
        self.filters_tab.setAutoFillBackground(False)
        self.filters = QFrame(self.filters_tab)
        self.filters.setObjectName(u"filters")
        self.filters.setEnabled(True)
        self.filters.setGeometry(QRect(10, 10, 301, 481))
        self.filters.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.filters.setFrameShape(QFrame.StyledPanel)
        self.filters.setFrameShadow(QFrame.Raised)
        self.filter_page_0 = QGroupBox(self.filters)
        self.filter_page_0.setObjectName(u"filter_page_0")
        self.filter_page_0.setEnabled(False)
        self.filter_page_0.setGeometry(QRect(10, 10, 281, 461))
        self.filter_page_0.setAutoFillBackground(False)
        self.filter_page_0.setStyleSheet(u"QGroupBox { \n"
"	border: none;\n"
"	border-width: 0px;\n"
"}")
        self.black_white = QPushButton(self.filter_page_0)
        self.black_white.setObjectName(u"black_white")
        self.black_white.setGeometry(QRect(10, 10, 261, 41))
        self.black_white.setCursor(QCursor(Qt.PointingHandCursor))
        self.black_white.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.negative = QPushButton(self.filter_page_0)
        self.negative.setObjectName(u"negative")
        self.negative.setGeometry(QRect(10, 60, 261, 41))
        self.negative.setCursor(QCursor(Qt.PointingHandCursor))
        self.negative.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_red = QPushButton(self.filter_page_0)
        self.inversion_red.setObjectName(u"inversion_red")
        self.inversion_red.setGeometry(QRect(10, 110, 261, 41))
        self.inversion_red.setCursor(QCursor(Qt.PointingHandCursor))
        self.inversion_red.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_green = QPushButton(self.filter_page_0)
        self.inversion_green.setObjectName(u"inversion_green")
        self.inversion_green.setGeometry(QRect(10, 160, 261, 41))
        self.inversion_green.setCursor(QCursor(Qt.PointingHandCursor))
        self.inversion_green.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_blue = QPushButton(self.filter_page_0)
        self.inversion_blue.setObjectName(u"inversion_blue")
        self.inversion_blue.setGeometry(QRect(10, 210, 261, 41))
        self.inversion_blue.setCursor(QCursor(Qt.PointingHandCursor))
        self.inversion_blue.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.black_gray_white = QPushButton(self.filter_page_0)
        self.black_gray_white.setObjectName(u"black_gray_white")
        self.black_gray_white.setGeometry(QRect(10, 260, 261, 41))
        self.black_gray_white.setCursor(QCursor(Qt.PointingHandCursor))
        self.black_gray_white.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.retro = QPushButton(self.filter_page_0)
        self.retro.setObjectName(u"retro")
        self.retro.setGeometry(QRect(10, 310, 261, 41))
        self.retro.setCursor(QCursor(Qt.PointingHandCursor))
        self.retro.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.neon_retro = QPushButton(self.filter_page_0)
        self.neon_retro.setObjectName(u"neon_retro")
        self.neon_retro.setGeometry(QRect(10, 360, 261, 41))
        self.neon_retro.setCursor(QCursor(Qt.PointingHandCursor))
        self.neon_retro.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.sakura = QPushButton(self.filter_page_0)
        self.sakura.setObjectName(u"sakura")
        self.sakura.setGeometry(QRect(10, 410, 261, 41))
        self.sakura.setCursor(QCursor(Qt.PointingHandCursor))
        self.sakura.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filter_page_1 = QGroupBox(self.filters)
        self.filter_page_1.setObjectName(u"filter_page_1")
        self.filter_page_1.setEnabled(False)
        self.filter_page_1.setGeometry(QRect(10, 10, 281, 461))
        self.filter_page_1.setAutoFillBackground(False)
        self.filter_page_1.setStyleSheet(u"QGroupBox { \n"
"	border: none;\n"
"	border-width: 0px;\n"
"}")
        self.total_black_white = QPushButton(self.filter_page_1)
        self.total_black_white.setObjectName(u"total_black_white")
        self.total_black_white.setGeometry(QRect(10, 10, 261, 41))
        self.total_black_white.setCursor(QCursor(Qt.PointingHandCursor))
        self.total_black_white.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.contour = QPushButton(self.filter_page_1)
        self.contour.setObjectName(u"contour")
        self.contour.setEnabled(False)
        self.contour.setGeometry(QRect(10, 60, 261, 41))
        self.contour.setCursor(QCursor(Qt.PointingHandCursor))
        self.contour.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.white_balance = QPushButton(self.filter_page_1)
        self.white_balance.setObjectName(u"white_balance")
        self.white_balance.setGeometry(QRect(10, 110, 261, 41))
        self.white_balance.setCursor(QCursor(Qt.PointingHandCursor))
        self.white_balance.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.black_balance = QPushButton(self.filter_page_1)
        self.black_balance.setObjectName(u"black_balance")
        self.black_balance.setGeometry(QRect(10, 160, 261, 41))
        self.black_balance.setCursor(QCursor(Qt.PointingHandCursor))
        self.black_balance.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.retro_2 = QPushButton(self.filter_page_1)
        self.retro_2.setObjectName(u"retro_2")
        self.retro_2.setEnabled(False)
        self.retro_2.setGeometry(QRect(10, 210, 261, 41))
        self.retro_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.retro_2.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.neon_retro_2 = QPushButton(self.filter_page_1)
        self.neon_retro_2.setObjectName(u"neon_retro_2")
        self.neon_retro_2.setEnabled(False)
        self.neon_retro_2.setGeometry(QRect(10, 260, 261, 41))
        self.neon_retro_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.neon_retro_2.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filters_nav_first = QPushButton(self.filters_tab)
        self.filters_nav_first.setObjectName(u"filters_nav_first")
        self.filters_nav_first.setGeometry(QRect(20, 500, 41, 41))
        self.filters_nav_first.setCursor(QCursor(Qt.PointingHandCursor))
        self.filters_nav_first.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filters_nav_prev = QPushButton(self.filters_tab)
        self.filters_nav_prev.setObjectName(u"filters_nav_prev")
        self.filters_nav_prev.setGeometry(QRect(70, 500, 41, 41))
        self.filters_nav_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.filters_nav_prev.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filters_nav_next = QPushButton(self.filters_tab)
        self.filters_nav_next.setObjectName(u"filters_nav_next")
        self.filters_nav_next.setGeometry(QRect(210, 500, 41, 41))
        self.filters_nav_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.filters_nav_next.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filters_nav_last = QPushButton(self.filters_tab)
        self.filters_nav_last.setObjectName(u"filters_nav_last")
        self.filters_nav_last.setGeometry(QRect(260, 500, 41, 41))
        self.filters_nav_last.setCursor(QCursor(Qt.PointingHandCursor))
        self.filters_nav_last.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.filters_page = QLabel(self.filters_tab)
        self.filters_page.setObjectName(u"filters_page")
        self.filters_page.setGeometry(QRect(120, 510, 81, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filters_page.setFont(font)
        self.filters_page.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.filters_tab, "")
        self.presets_tab = QWidget()
        self.presets_tab.setObjectName(u"presets_tab")
        self.presets = QFrame(self.presets_tab)
        self.presets.setObjectName(u"presets")
        self.presets.setEnabled(True)
        self.presets.setGeometry(QRect(10, 10, 300, 181))
        self.presets.setStyleSheet(u"background-color: rgb(47, 47, 47);\n"
"border-radius: 25px;\n"
"border: 1px solid #fff;")
        self.presets.setFrameShape(QFrame.StyledPanel)
        self.presets.setFrameShadow(QFrame.Raised)
        self.commit_preset = QPushButton(self.presets)
        self.commit_preset.setObjectName(u"commit_preset")
        self.commit_preset.setEnabled(False)
        self.commit_preset.setGeometry(QRect(20, 120, 261, 41))
        self.commit_preset.setCursor(QCursor(Qt.PointingHandCursor))
        self.commit_preset.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.preset_box = QComboBox(self.presets)
        self.preset_box.setObjectName(u"preset_box")
        self.preset_box.setEnabled(False)
        self.preset_box.setGeometry(QRect(20, 70, 261, 41))
        self.preset_box.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #fff;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}\n"
"\n"
"QComboBox:drop-down{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border-radius: 10px;\n"
"    selection-background-color: lightgray;\n"
"}")
        self.create_preset = QPushButton(self.presets)
        self.create_preset.setObjectName(u"create_preset")
        self.create_preset.setGeometry(QRect(20, 20, 261, 41))
        self.create_preset.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_preset.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.tabWidget.addTab(self.presets_tab, "")
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(350, 10, 580, 580))
        self.img.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: solid #fff;\n"
"border-radius: 25px;")
        self.log = QLabel(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setEnabled(True)
        self.log.setGeometry(QRect(20, 600, 901, 24))
        self.log.setAutoFillBackground(False)
        self.log.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 5px\n"
"}")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Photoshop", None))
        self.img_link.setText("")
        self.img_link.setPlaceholderText(QCoreApplication.translate("Window", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.img_dl.setText(QCoreApplication.translate("Window", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.open.setText(QCoreApplication.translate("Window", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.open.setShortcut(QCoreApplication.translate("Window", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.close.setText(QCoreApplication.translate("Window", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.save.setText(QCoreApplication.translate("Window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.save_as.setText(QCoreApplication.translate("Window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file_tab), QCoreApplication.translate("Window", u"\u0424\u0430\u0439\u043b", None))
        self.red_circle.setText("")
        self.green_circle.setText("")
        self.blue_circle.setText("")
        self.channels_reset.setText(QCoreApplication.translate("Window", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.channels_commit.setText(QCoreApplication.translate("Window", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.green_toggler.setText(QCoreApplication.translate("Window", u"\u0417\u0435\u043b\u0451\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b", None))
        self.blue_toggler.setText(QCoreApplication.translate("Window", u"\u0421\u0438\u043d\u0438\u0439 \u043a\u0430\u043d\u0430\u043b", None))
        self.red_toggler.setText(QCoreApplication.translate("Window", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b", None))
        self.togglers_commit.setText(QCoreApplication.translate("Window", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.channels_tab), QCoreApplication.translate("Window", u"\u041a\u0430\u043d\u0430\u043b\u044b", None))
        self.filter_page_0.setTitle("")
        self.black_white.setText(QCoreApplication.translate("Window", u"\u0427\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.negative.setText(QCoreApplication.translate("Window", u"\u041d\u0435\u0433\u0430\u0442\u0438\u0432", None))
        self.inversion_red.setText(QCoreApplication.translate("Window", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.inversion_green.setText(QCoreApplication.translate("Window", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u0437\u0435\u043b\u0451\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.inversion_blue.setText(QCoreApplication.translate("Window", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u0441\u0438\u043d\u0435\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.black_gray_white.setText(QCoreApplication.translate("Window", u"\u0427\u0451\u0440\u043d\u043e-\u0441\u0435\u0440\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.retro.setText(QCoreApplication.translate("Window", u"\u0420\u0435\u0442\u0440\u043e", None))
        self.neon_retro.setText(QCoreApplication.translate("Window", u"\u041d\u0435\u043e\u043d\u043e\u0432\u044b\u0439 \u0440\u0435\u0442\u0440\u043e", None))
        self.sakura.setText(QCoreApplication.translate("Window", u"\u0421\u0430\u043a\u0443\u0440\u0430", None))
        self.filter_page_1.setTitle("")
        self.total_black_white.setText(QCoreApplication.translate("Window", u"\u0410\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u043e \u0447\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.contour.setText(QCoreApplication.translate("Window", u"\u041a\u043e\u043d\u0442\u0443\u0440", None))
        self.white_balance.setText(QCoreApplication.translate("Window", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0431\u0435\u043b\u043e\u0433\u043e", None))
        self.black_balance.setText(QCoreApplication.translate("Window", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0447\u0451\u0440\u043d\u043e\u0433\u043e", None))
        self.retro_2.setText(QCoreApplication.translate("Window", u"\u0425\u0440\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0430\u0431\u0431\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.neon_retro_2.setText(QCoreApplication.translate("Window", u"\u0420\u043e\u0437\u043e\u0432\u044b\u0435 \u043e\u0447\u043a\u0438", None))
        self.filters_nav_first.setText(QCoreApplication.translate("Window", u"<<", None))
        self.filters_nav_prev.setText(QCoreApplication.translate("Window", u"<", None))
        self.filters_nav_next.setText(QCoreApplication.translate("Window", u">", None))
        self.filters_nav_last.setText(QCoreApplication.translate("Window", u">>", None))
        self.filters_page.setText(QCoreApplication.translate("Window", u"NaN/NaN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filters_tab), QCoreApplication.translate("Window", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        self.commit_preset.setText(QCoreApplication.translate("Window", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.create_preset.setText(QCoreApplication.translate("Window", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.presets_tab), QCoreApplication.translate("Window", u"\u041f\u0440\u0435\u0441\u0435\u0442\u044b", None))
        self.img.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.log.setText("")
    # retranslateUi


class PresetDialog:
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 540)
        Dialog.setMinimumSize(QSize(580, 540))
        Dialog.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.name = QLineEdit(Dialog)
        self.name.setObjectName(u"name")
        self.name.setEnabled(True)
        self.name.setGeometry(QRect(20, 20, 541, 41))
        self.name.setText("Название")
        self.name.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"	border: 1px solid #5865F2;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.black_white = QCheckBox(Dialog)
        self.black_white.setObjectName(u"black_white")
        self.black_white.setGeometry(QRect(20, 70, 261, 41))
        self.black_white.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.negative = QCheckBox(Dialog)
        self.negative.setObjectName(u"negative")
        self.negative.setGeometry(QRect(300, 70, 261, 41))
        self.negative.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_red = QCheckBox(Dialog)
        self.inversion_red.setObjectName(u"inversion_red")
        self.inversion_red.setGeometry(QRect(20, 120, 261, 41))
        self.inversion_red.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_green = QCheckBox(Dialog)
        self.inversion_green.setObjectName(u"inversion_green")
        self.inversion_green.setGeometry(QRect(300, 120, 261, 41))
        self.inversion_green.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.inversion_blue = QCheckBox(Dialog)
        self.inversion_blue.setObjectName(u"inversion_blue")
        self.inversion_blue.setGeometry(QRect(20, 170, 261, 41))
        self.inversion_blue.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.black_gray_white = QCheckBox(Dialog)
        self.black_gray_white.setObjectName(u"black_gray_white")
        self.black_gray_white.setGeometry(QRect(300, 170, 261, 41))
        self.black_gray_white.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.retro = QCheckBox(Dialog)
        self.retro.setObjectName(u"retro")
        self.retro.setGeometry(QRect(20, 220, 261, 41))
        self.retro.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.neon_retro = QCheckBox(Dialog)
        self.neon_retro.setObjectName(u"neon_retro")
        self.neon_retro.setGeometry(QRect(300, 220, 261, 41))
        self.neon_retro.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.sakura = QCheckBox(Dialog)
        self.sakura.setObjectName(u"sakura")
        self.sakura.setGeometry(QRect(20, 270, 261, 41))
        self.sakura.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.total_black_white = QCheckBox(Dialog)
        self.total_black_white.setObjectName(u"total_black_white")
        self.total_black_white.setGeometry(QRect(300, 270, 261, 41))
        self.total_black_white.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.contour = QCheckBox(Dialog)
        self.contour.setObjectName(u"contour")
        self.contour.setEnabled(False)
        self.contour.setGeometry(QRect(20, 320, 261, 41))
        self.contour.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.white_balance = QCheckBox(Dialog)
        self.white_balance.setObjectName(u"white_balance")
        self.white_balance.setGeometry(QRect(300, 320, 261, 41))
        self.white_balance.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.black_balance = QCheckBox(Dialog)
        self.black_balance.setObjectName(u"black_balance")
        self.black_balance.setGeometry(QRect(20, 370, 261, 41))
        self.black_balance.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.checkBox_14 = QCheckBox(Dialog)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setEnabled(False)
        self.checkBox_14.setGeometry(QRect(300, 370, 261, 41))
        self.checkBox_14.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.checkBox_15 = QCheckBox(Dialog)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setEnabled(False)
        self.checkBox_15.setGeometry(QRect(160, 420, 261, 41))
        self.checkBox_15.setStyleSheet(u"QCheckBox{\n"
"	padding-left: 10px;\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")
        self.create = QPushButton(Dialog)
        self.create.setObjectName(u"create")
        self.create.setEnabled(False)
        self.create.setGeometry(QRect(20, 480, 541, 41))
        self.create.setCursor(QCursor(Qt.PointingHandCursor))
        self.create.setStyleSheet(u"QPushButton {\n"
"	border: solid #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-color: #5865F2;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-color: gray;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0441\u0435\u0442\u0430", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.black_white.setText(QCoreApplication.translate("Dialog", u"\u0427\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.negative.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0433\u0430\u0442\u0438\u0432", None))
        self.inversion_red.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.inversion_green.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u0437\u0435\u043b\u0451\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.inversion_blue.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0432\u0435\u0440\u0441\u0438\u044f \u0441\u0438\u043d\u0435\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.black_gray_white.setText(QCoreApplication.translate("Dialog", u"\u0427\u0451\u0440\u043d\u043e-\u0441\u0435\u0440\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.retro.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0442\u0440\u043e", None))
        self.neon_retro.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u043e\u043d\u043e\u0432\u044b\u0439 \u0440\u0435\u0442\u0440\u043e", None))
        self.sakura.setText(QCoreApplication.translate("Dialog", u"\u0421\u0430\u043a\u0443\u0440\u0430", None))
        self.total_black_white.setText(QCoreApplication.translate("Dialog", u"\u0410\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u043e \u0447\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.contour.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0442\u0443\u0440", None))
        self.white_balance.setText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0431\u0435\u043b\u043e\u0433\u043e", None))
        self.black_balance.setText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0447\u0451\u0440\u043d\u043e\u0433\u043e", None))
        self.checkBox_14.setText(QCoreApplication.translate("Dialog", u"\u0425\u0440\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0430\u0431\u0431\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.checkBox_15.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u0437\u043e\u0432\u044b\u0435 \u043e\u0447\u043a\u0438", None))
        self.create.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi


