# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_encuesta.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_SO = QtWidgets.QLabel(self.centralwidget)
        self.etq_SO.setGeometry(QtCore.QRect(40, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_SO.setFont(font)
        self.etq_SO.setObjectName("etq_SO")
        self.radioWindows = QtWidgets.QRadioButton(self.centralwidget)
        self.radioWindows.setGeometry(QtCore.QRect(40, 80, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioWindows.setFont(font)
        self.radioWindows.setObjectName("radioWindows")
        self.radioLinux = QtWidgets.QRadioButton(self.centralwidget)
        self.radioLinux.setGeometry(QtCore.QRect(40, 120, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioLinux.setFont(font)
        self.radioLinux.setObjectName("radioLinux")
        self.radioMac = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMac.setGeometry(QtCore.QRect(40, 160, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioMac.setFont(font)
        self.radioMac.setObjectName("radioMac")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 200, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.etq_especialidad = QtWidgets.QLabel(self.centralwidget)
        self.etq_especialidad.setGeometry(QtCore.QRect(40, 230, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_especialidad.setFont(font)
        self.etq_especialidad.setObjectName("etq_especialidad")
        self.checkProgramacion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkProgramacion.setGeometry(QtCore.QRect(40, 280, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkProgramacion.setFont(font)
        self.checkProgramacion.setObjectName("checkProgramacion")
        self.checkDisenyo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDisenyo.setGeometry(QtCore.QRect(40, 320, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkDisenyo.setFont(font)
        self.checkDisenyo.setObjectName("checkDisenyo")
        self.checkAdministracion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAdministracion.setGeometry(QtCore.QRect(40, 360, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkAdministracion.setFont(font)
        self.checkAdministracion.setObjectName("checkAdministracion")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 410, 311, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.etq_horas = QtWidgets.QLabel(self.centralwidget)
        self.etq_horas.setGeometry(QtCore.QRect(40, 440, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_horas.setFont(font)
        self.etq_horas.setObjectName("etq_horas")
        self.sliderHoras = QtWidgets.QSlider(self.centralwidget)
        self.sliderHoras.setGeometry(QtCore.QRect(40, 500, 281, 22))
        self.sliderHoras.setMinimum(0)
        self.sliderHoras.setMaximum(10)
        self.sliderHoras.setSliderPosition(5)
        self.sliderHoras.setTracking(True)
        self.sliderHoras.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHoras.setInvertedControls(False)
        self.sliderHoras.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sliderHoras.setTickInterval(1)
        self.sliderHoras.setObjectName("sliderHoras")
        self.botonGenerar = QtWidgets.QPushButton(self.centralwidget)
        self.botonGenerar.setGeometry(QtCore.QRect(110, 560, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.botonGenerar.setFont(font)
        self.botonGenerar.setObjectName("botonGenerar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Encuesta"))
        self.etq_SO.setText(_translate("MainWindow", "Elige un sistema operativo "))
        self.radioWindows.setText(_translate("MainWindow", "Windows"))
        self.radioLinux.setText(_translate("MainWindow", "Linux"))
        self.radioMac.setText(_translate("MainWindow", "Mac"))
        self.etq_especialidad.setText(_translate("MainWindow", "Elige tu especialidad"))
        self.checkProgramacion.setText(_translate("MainWindow", "Programación"))
        self.checkDisenyo.setText(_translate("MainWindow", "Diseño gráfico"))
        self.checkAdministracion.setText(_translate("MainWindow", "Administración"))
        self.etq_horas.setText(_translate("MainWindow", "Horas que dedicas en el ordenador"))
        self.botonGenerar.setText(_translate("MainWindow", "Generar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
