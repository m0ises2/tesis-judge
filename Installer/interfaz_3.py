# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_3.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_instalador_interfaz_3(object):
    def setupUi(self, instalador_interfaz_3):
        instalador_interfaz_3.setObjectName("instalador_interfaz_3")
        instalador_interfaz_3.setEnabled(True)
        instalador_interfaz_3.resize(684, 454)
        instalador_interfaz_3.setMinimumSize(QtCore.QSize(684, 454))
        instalador_interfaz_3.setMaximumSize(QtCore.QSize(684, 454))
        self.facyt_logo = QtWidgets.QLabel(instalador_interfaz_3)
        self.facyt_logo.setGeometry(QtCore.QRect(40, 220, 141, 161))
        self.facyt_logo.setText("")
        self.facyt_logo.setPixmap(QtGui.QPixmap("assets/facyt.png"))
        self.facyt_logo.setScaledContents(True)
        self.facyt_logo.setObjectName("facyt_logo")
        self.uc_logo = QtWidgets.QLabel(instalador_interfaz_3)
        self.uc_logo.setGeometry(QtCore.QRect(50, 40, 111, 161))
        self.uc_logo.setText("")
        self.uc_logo.setPixmap(QtGui.QPixmap("assets/log_uc.png"))
        self.uc_logo.setScaledContents(True)
        self.uc_logo.setObjectName("uc_logo")
        self.layoutWidget = QtWidgets.QWidget(instalador_interfaz_3)
        self.layoutWidget.setGeometry(QtCore.QRect(195, 11, 481, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(-1, -1, 3, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_principal = QtWidgets.QLabel(self.layoutWidget)
        self.label_principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_principal.setStyleSheet("font: 63 bold 22pt \"Ubuntu\";")
        self.label_principal.setMidLineWidth(-3)
        self.label_principal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_principal.setWordWrap(True)
        self.label_principal.setObjectName("label_principal")
        self.verticalLayout.addWidget(self.label_principal)
        self.label_descripcion = QtWidgets.QLabel(self.layoutWidget)
        self.label_descripcion.setWordWrap(True)
        self.label_descripcion.setObjectName("label_descripcion")
        self.verticalLayout.addWidget(self.label_descripcion)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_usuario = QtWidgets.QLabel(self.layoutWidget)
        self.label_usuario.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";")
        self.label_usuario.setObjectName("label_usuario")
        self.gridLayout.addWidget(self.label_usuario, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        self.label_contrasenha = QtWidgets.QLabel(self.layoutWidget)
        self.label_contrasenha.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";")
        self.label_contrasenha.setObjectName("label_contrasenha")
        self.gridLayout.addWidget(self.label_contrasenha, 3, 0, 1, 2)
        self.contrasenha = QtWidgets.QLabel(self.layoutWidget)
        self.contrasenha.setAlignment(QtCore.Qt.AlignCenter)
        self.contrasenha.setObjectName("contrasenha")
        self.gridLayout.addWidget(self.contrasenha, 3, 3, 1, 1)
        self.usuario = QtWidgets.QLabel(self.layoutWidget)
        self.usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.usuario.setObjectName("usuario")
        self.gridLayout.addWidget(self.usuario, 1, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 158, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.anterior_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.anterior_3.setEnabled(True)
        self.anterior_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.anterior_3.setAutoDefault(True)
        self.anterior_3.setObjectName("anterior_3")
        self.horizontalLayout_2.addWidget(self.anterior_3)
        self.instalar = QtWidgets.QPushButton(self.layoutWidget)
        self.instalar.setEnabled(True)
        self.instalar.setObjectName("instalar")
        self.horizontalLayout_2.addWidget(self.instalar)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.cancelar_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelar_3.setObjectName("cancelar_3")
        self.horizontalLayout_2.addWidget(self.cancelar_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(instalador_interfaz_3)
        QtCore.QMetaObject.connectSlotsByName(instalador_interfaz_3)

    def retranslateUi(self, instalador_interfaz_3):
        _translate = QtCore.QCoreApplication.translate
        instalador_interfaz_3.setWindowTitle(_translate("instalador_interfaz_3", "OJ+ Instalador - Instalar"))
        self.label_principal.setText(_translate("instalador_interfaz_3", "Todo listo para iniciar la instalación."))
        self.label_descripcion.setText(_translate("instalador_interfaz_3", "Pulse instalar para iniciar el proceso de instalación del Juez OJ+ en su computador con la siguiente configuración:"))
        self.label_usuario.setText(_translate("instalador_interfaz_3", "Usuario:"))
        self.label_contrasenha.setText(_translate("instalador_interfaz_3", "Contraseña:"))
        self.contrasenha.setText(_translate("instalador_interfaz_3", "123456"))
        self.usuario.setText(_translate("instalador_interfaz_3", "Daniel-juez"))
        self.anterior_3.setText(_translate("instalador_interfaz_3", "Anterior"))
        self.instalar.setText(_translate("instalador_interfaz_3", "Instalar"))
        self.cancelar_3.setText(_translate("instalador_interfaz_3", "Cancelar"))

