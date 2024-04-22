# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastroClienteController.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from model.dao.ClienteDAO import ClienteDAO
from model.domain.Cliente import Cliente
from model.domain.Endereco import Endereco


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 768)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-40, -10, 251, 781))
        self.frame.setStyleSheet("background-color: rgb(56, 104, 106);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 30, 341, 51))
        self.label.setStyleSheet("font: 75 24pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 120, 461, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.input_nome = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_nome.setObjectName("input_nome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_nome)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(240, 210, 461, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.input_sobrenome = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_sobrenome.setObjectName("input_sobrenome")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_sobrenome)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(240, 310, 182, 59))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_4.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.input_date = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.input_date.setObjectName("input_date")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_date)
        self.formLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(240, 410, 181, 61))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_5.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.input_telefone = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.input_telefone.setObjectName("input_telefone")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_telefone)
        self.formLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(240, 500, 181, 61))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_6.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.input_cpf = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.input_cpf.setObjectName("input_cpf")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_cpf)
        self.formLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(240, 600, 90, 30))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_7.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(880, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(560, 690, 33, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(820, 690, 13, 13))
        self.label_12.setObjectName("label_12")
        self.input_rua = QtWidgets.QLineEdit(Dialog)
        self.input_rua.setGeometry(QtCore.QRect(280, 650, 381, 24))
        self.input_rua.setObjectName("input_rua")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(680, 650, 37, 16))
        self.label_9.setObjectName("label_9")
        self.input_numero = QtWidgets.QLineEdit(Dialog)
        self.input_numero.setGeometry(QtCore.QRect(730, 650, 71, 24))
        self.input_numero.setObjectName("input_numero")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(240, 690, 28, 13))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(241, 651, 19, 16))
        self.label_8.setObjectName("label_8")
        self.input_uf = QtWidgets.QLineEdit(Dialog)
        self.input_uf.setGeometry(QtCore.QRect(840, 680, 131, 24))
        self.input_uf.setObjectName("input_uf")
        self.input_bairro = QtWidgets.QLineEdit(Dialog)
        self.input_bairro.setGeometry(QtCore.QRect(280, 680, 261, 24))
        self.input_bairro.setObjectName("input_bairro")
        self.input_cidade = QtWidgets.QLineEdit(Dialog)
        self.input_cidade.setGeometry(QtCore.QRect(601, 680, 211, 24))
        self.input_cidade.setObjectName("input_cidade")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.inserir_dados)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Cadastro de Cliente"))
        self.label_2.setText(_translate("Dialog", "Nome"))
        self.label_3.setText(_translate("Dialog", "Sobrenome"))
        self.label_4.setText(_translate("Dialog", "Data de nascimento"))
        self.label_5.setText(_translate("Dialog", "Telefone de contato"))
        self.label_6.setText(_translate("Dialog", "CPF"))
        self.label_7.setText(_translate("Dialog", "Endereço"))
        self.pushButton.setText(_translate("Dialog", "Finalizar cadastro"))
        self.label_11.setText(_translate("Dialog", "Cidade"))
        self.label_12.setText(_translate("Dialog", "UF"))
        self.label_9.setText(_translate("Dialog", "Numero"))
        self.label_10.setText(_translate("Dialog", "Bairro"))
        self.label_8.setText(_translate("Dialog", "Rua"))
        
    def inserir_dados(self):
        clienteDAO = ClienteDAO()
        cliente = Cliente()
        endereco = Endereco()
        
        cliente.nome = self.input_nome.text()
        cliente.sobrenome = self.input_sobrenome.text()
        cliente.data_nascimento = self.input_date.text()
        cliente.tel_contato = self.input_telefone.text()
        cliente.cpf = self.input_cpf.text()
        cliente.data_cadastro = datetime.date.today()
        
        # Endereço do cliente
        endereco.rua = self.input_rua.text()
        endereco.numero = self.input_numero.text()
        endereco.bairro = self.input_bairro.text()
        endereco.cidade = self.input_cidade.text()
        endereco.uf = self.input_uf.text()
        cliente.endereco = endereco
        
        clienteDAO.insert(cliente)
        # print("teste")