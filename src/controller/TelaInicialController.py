# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TelaInicialView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from model.domain.Usuario import Usuario
from model.dao.UsuarioDAO import UsuarioDAO
from model.database.BaseDAO import BaseDAO
from controller.TelaPrincipalController import Ui_MainWindow as TelaPrincipal, MainWindow

class Ui_widget_login(object):

    session = BaseDAO.get_session()
    usuario_dao = UsuarioDAO(session)
    
    def setupUi(self, widget_login):

        widget_login.setObjectName("widget_login")
        widget_login.resize(1065, 586)
        widget_login.setStyleSheet("background-color: #38686A")
        self.frame = QtWidgets.QFrame(widget_login)
        self.frame.setGeometry(QtCore.QRect(350, 120, 351, 301))
        self.frame.setStyleSheet("background-color: #fafafa;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_entrar = QtWidgets.QPushButton(self.frame)
        self.button_entrar.setGeometry(QtCore.QRect(130, 250, 93, 28))
        self.button_entrar.setStyleSheet("background-color: #A3B4A2;\n"
"color: white;")
        self.button_entrar.setObjectName("button_entrar")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(20, 60, 311, 151))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setStyleSheet("font-size: 16px;\n"
"font-family: \'Segoe UI\';")
        self.label.setObjectName("label")
        self.insert_nome_usuario = QtWidgets.QLineEdit(self.splitter)
        self.insert_nome_usuario.setObjectName("insert_nome_usuario")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setStyleSheet("font-size: 16px;\n"
"font-family: \'Segoe UI\';")
        self.label_2.setObjectName("label_2")
        self.insert_senha_usuario = QtWidgets.QLineEdit(self.splitter)
        self.insert_senha_usuario.setObjectName("insert_senha_usuario")
        self.insert_senha_usuario.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dados_invalidos = QtWidgets.QLabel(self.frame)
        self.dados_invalidos.setObjectName(u"dados_invalidos")
        self.dados_invalidos.setGeometry(QtCore.QRect(55,220,261,16))
        self.dados_invalidos.setStyleSheet(u"color: red; text-align: center;")

        self.retranslateUi(widget_login)
        QtCore.QMetaObject.connectSlotsByName(widget_login)
        
    def retranslateUi(self, widget_login):
        _translate = QtCore.QCoreApplication.translate
        widget_login.setWindowTitle(_translate("widget_login", "Form"))
        self.button_entrar.setText(_translate("widget_login", "Entrar"))
        self.label.setText(_translate("widget_login", "Nome de usuário"))
        self.label_2.setText(_translate("widget_login", "Senha"))

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carregue a interface .ui
        loadUi('src/view/TelaInicialView.ui', self)
        # Conecte os sinais aos slots
        self.button_entrar.clicked.connect(self.login)

    def login(self):
        session = BaseDAO.get_session()
        usuario_dao = UsuarioDAO(session)
        usuario = Usuario()
        
        usuario.nome_usuario = self.insert_nome_usuario.text()
        usuario.senha_usuario = self.insert_senha_usuario.text()
        
        if (usuario_dao.verifica_usuario(usuario) == 0):
            self.dados_invalidos.setText("Dados inválidos. Por gentileza, revise-os.")
        else:
            self.openMainWindow()

    def openMainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.close()