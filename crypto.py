from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

from PyQt6 import QtCore, QtGui, QtWidgets

from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import draw_charts

class MplWidget(QWidget):
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 581, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 110, 573, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_crypto = QtWidgets.QLabel(self.layoutWidget1)
        self.label_crypto.setMinimumSize(QtCore.QSize(230, 0))

        self.comboBox.currentTextChanged.connect(self.aktualna_cena)

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_crypto.setFont(font)
        self.label_crypto.setObjectName("label_crypto")
        self.horizontalLayout_2.addWidget(self.label_crypto)
        spacerItem = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_price = QtWidgets.QLabel(self.layoutWidget1)
        self.label_price.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.horizontalLayout_2.addWidget(self.label_price)
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(50, 180, 701, 391))
        self.MplWidget.setObjectName("MplWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def aktualna_cena(self):
        cg = CoinGeckoAPI()
        item = self.comboBox.currentText()
        if item == "BTC":
            btc = cg.get_price(ids = 'bitcoin', vs_currencies = 'pln')
            self.label_crypto.setText('BTC kosztuje: ')
            self.label_price.setText(str(btc['bitcoin']['pln']) + ' zł')
            btcplot = draw_charts.market_info_btc
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(btcplot['timestamp'], btcplot['price'])
            self.MplWidget.canvas.draw()
        if item == "USDT":
            usdt = cg.get_price(ids = 'tether', vs_currencies= 'pln')
            self.label_crypto.setText('USDT kosztuje: ')
            self.label_price.setText(str(usdt['tether']['pln']) + ' zł')
            usdtplot = draw_charts.market_info_usdt
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(usdtplot['timestamp'], usdtplot['price'])
            self.MplWidget.canvas.draw()
        if item == "BCC":
            bcc = cg.get_price(ids = 'bitcoin-cash', vs_currencies= 'pln')
            self.label_crypto.setText('BCC kosztuje: ')
            self.label_price.setText(str(bcc['bitcoin-cash']['pln']) + ' zł')
            bccplot = draw_charts.market_info_bcc
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(bccplot['timestamp'], bccplot['price'])
            self.MplWidget.canvas.draw()
        if item == "DogeCoin":
            dogecoin = cg.get_price(ids = 'dogecoin', vs_currencies= 'pln')
            self.label_crypto.setText('DogeCoin kosztuje: ')
            self.label_price.setText(str(dogecoin['dogecoin']['pln']) + ' zł')
            dogeplot = draw_charts.market_info_doge
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(dogeplot['timestamp'], dogeplot['price'])
            self.MplWidget.canvas.draw()
        if item == "LUNA":
            luna = cg.get_price(ids = 'terra-luna', vs_currencies= 'pln')
            self.label_crypto.setText('Luna kosztuje: ')
            self.label_price.setText(str(luna['terra-luna']['pln']) + ' zł')
            lunaplot = draw_charts.market_info_luna
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(lunaplot['timestamp'], lunaplot['price'])
            self.MplWidget.canvas.draw()
        if item == "ETH":
            ethereum = cg.get_price(ids = 'ethereum', vs_currencies= 'pln')
            self.label_crypto.setText('Ethereum kosztuje: ')
            self.label_price.setText(str(ethereum['ethereum']['pln']) + ' pln')
            ethplot = draw_charts.market_info_eth
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(ethplot['timestamp'], ethplot['price'])
            self.MplWidget.canvas.draw()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Wybierz kryptowalute:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "BTC"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ETH"))
        self.comboBox.setItemText(2, _translate("MainWindow", "USDT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "BCC"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DogeCoin"))
        self.comboBox.setItemText(5, _translate("MainWindow", "LUNA"))
        self.label_crypto.setText(_translate("MainWindow", "TextLabel"))
        self.label_price.setText(_translate("MainWindow", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
