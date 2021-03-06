# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_instalador_interfaz_2(object):
    def setupUi(self, instalador_interfaz_2):
        instalador_interfaz_2.setObjectName("instalador_interfaz_2")
        instalador_interfaz_2.setEnabled(True)
        instalador_interfaz_2.resize(684, 454)
        instalador_interfaz_2.setMinimumSize(QtCore.QSize(684, 454))
        instalador_interfaz_2.setMaximumSize(QtCore.QSize(684, 454))
        self.facyt_logo = QtWidgets.QLabel(instalador_interfaz_2)
        self.facyt_logo.setGeometry(QtCore.QRect(40, 220, 141, 161))
        self.facyt_logo.setText("")
        self.facyt_logo.setPixmap(QtGui.QPixmap("assets/facyt.png"))
        self.facyt_logo.setScaledContents(True)
        self.facyt_logo.setObjectName("facyt_logo")
        self.uc_logo = QtWidgets.QLabel(instalador_interfaz_2)
        self.uc_logo.setGeometry(QtCore.QRect(50, 40, 111, 161))
        self.uc_logo.setText("")
        self.uc_logo.setPixmap(QtGui.QPixmap("assets/log_uc.png"))
        self.uc_logo.setScaledContents(True)
        self.uc_logo.setObjectName("uc_logo")
        self.layoutWidget = QtWidgets.QWidget(instalador_interfaz_2)
        self.layoutWidget.setGeometry(QtCore.QRect(192, 10, 481, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPrincipal = QtWidgets.QLabel(self.layoutWidget)
        self.labelPrincipal.setStyleSheet("font: 75 bold 22pt \"Ubuntu\";")
        self.labelPrincipal.setWordWrap(True)
        self.labelPrincipal.setObjectName("labelPrincipal")
        self.verticalLayout.addWidget(self.labelPrincipal)
        self.labelSegundaria = QtWidgets.QLabel(self.layoutWidget)
        self.labelSegundaria.setWordWrap(True)
        self.labelSegundaria.setObjectName("labelSegundaria")
        self.verticalLayout.addWidget(self.labelSegundaria)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.labelNomUsuario = QtWidgets.QLabel(self.layoutWidget)
        self.labelNomUsuario.setObjectName("labelNomUsuario")
        self.verticalLayout.addWidget(self.labelNomUsuario)
        spacerItem1 = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.LineUsuario = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineUsuario.setObjectName("LineUsuario")
        self.verticalLayout.addWidget(self.LineUsuario)
        self.labelUsuario = QtWidgets.QLabel(self.layoutWidget)
        self.labelUsuario.setText("")
        self.labelUsuario.setObjectName("labelUsuario")
        self.verticalLayout.addWidget(self.labelUsuario)
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelContrasenha = QtWidgets.QLabel(self.layoutWidget)
        self.labelContrasenha.setObjectName("labelContrasenha")
        self.verticalLayout.addWidget(self.labelContrasenha)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 63 9pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.contrasenha_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.contrasenha_1.setAcceptDrops(True)
        self.contrasenha_1.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.contrasenha_1.setInputMask("")
        self.contrasenha_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenha_1.setObjectName("contrasenha_1")
        self.verticalLayout.addWidget(self.contrasenha_1)
        self.labelREPContrasenah = QtWidgets.QLabel(self.layoutWidget)
        self.labelREPContrasenah.setObjectName("labelREPContrasenah")
        self.verticalLayout.addWidget(self.labelREPContrasenah)
        self.contrasenha_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.contrasenha_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenha_2.setObjectName("contrasenha_2")
        self.verticalLayout.addWidget(self.contrasenha_2)
        self.coincidencia = QtWidgets.QLabel(self.layoutWidget)
        self.coincidencia.setStyleSheet("font: 75 10pt \"Ubuntu\"; color:red")
        self.coincidencia.setText("")
        self.coincidencia.setObjectName("coincidencia")
        self.verticalLayout.addWidget(self.coincidencia)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.anterior_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.anterior_2.setEnabled(True)
        self.anterior_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.anterior_2.setAutoDefault(True)
        self.anterior_2.setObjectName("anterior_2")
        self.horizontalLayout_2.addWidget(self.anterior_2)
        self.siguiente_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.siguiente_2.setEnabled(False)
        self.siguiente_2.setObjectName("siguiente_2")
        self.horizontalLayout_2.addWidget(self.siguiente_2)
        spacerItem6 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.cancelar_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelar_2.setObjectName("cancelar_2")
        self.horizontalLayout_2.addWidget(self.cancelar_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.labelNomUsuario.setBuddy(self.LineUsuario)
        self.labelContrasenha.setBuddy(self.contrasenha_1)
        self.labelREPContrasenah.setBuddy(self.contrasenha_2)

        self.retranslateUi(instalador_interfaz_2)
        QtCore.QMetaObject.connectSlotsByName(instalador_interfaz_2)

    def retranslateUi(self, instalador_interfaz_2):
        _translate = QtCore.QCoreApplication.translate
        instalador_interfaz_2.setWindowTitle(_translate("instalador_interfaz_2", "OJ+ Instalador - Cuenta"))
        self.labelPrincipal.setText(_translate("instalador_interfaz_2", "Configuración de cuenta."))
        self.labelSegundaria.setText(_translate("instalador_interfaz_2", "Esta sección le permetirá configurar la cuenta de usuario del sistema para el juez OJ+"))
        self.labelNomUsuario.setText(_translate("instalador_interfaz_2", "Nombre de Usuario"))
        self.labelContrasenha.setText(_translate("instalador_interfaz_2", "Contraseña"))
        self.label.setText(_translate("instalador_interfaz_2", "Las mayúsculas serán convertidas a minúsculas"))
        self.labelREPContrasenah.setText(_translate("instalador_interfaz_2", "Repetir contraseña"))
        self.anterior_2.setText(_translate("instalador_interfaz_2", "Anterior"))
        self.siguiente_2.setText(_translate("instalador_interfaz_2", "Siguiente"))
        self.cancelar_2.setText(_translate("instalador_interfaz_2", "Cancelar"))

