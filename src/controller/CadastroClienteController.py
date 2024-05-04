# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/CadastroClienteView.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from model.dao.ClienteDAO import ClienteDAO
from model.domain.Cliente import Cliente
from model.domain.Endereco import Endereco
from model.database.BaseDAO import BaseDAO

class Ui_Form(object):
    session = BaseDAO.get_session()
    clienteDAO = ClienteDAO(session)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1065, 586)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(792, 70, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 0, 609, 558))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 75 24pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.input_nome = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_nome.setObjectName("input_nome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_nome)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.input_sobrenome = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_sobrenome.setObjectName("input_sobrenome")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_sobrenome)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.input_date = QtWidgets.QDateEdit(self.layoutWidget)
        self.input_date.setObjectName("input_date")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_date)
        self.horizontalLayout_6.addLayout(self.formLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.input_telefone = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_telefone.setObjectName("input_telefone")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_telefone)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.horizontalLayout_6.addLayout(self.formLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.input_cpf = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_cpf.setObjectName("input_cpf")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_cpf)
        self.horizontalLayout_6.addLayout(self.formLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(19, 24))
        self.label_8.setMaximumSize(QtCore.QSize(19, 24))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.input_rua = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_rua.setMinimumSize(QtCore.QSize(381, 24))
        self.input_rua.setMaximumSize(QtCore.QSize(381, 24))
        self.input_rua.setObjectName("input_rua")
        self.horizontalLayout.addWidget(self.input_rua, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(37, 24))
        self.label_9.setMaximumSize(QtCore.QSize(37, 24))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.input_numero = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_numero.setMinimumSize(QtCore.QSize(41, 24))
        self.input_numero.setMaximumSize(QtCore.QSize(41, 24))
        self.input_numero.setObjectName("input_numero")
        self.horizontalLayout_3.addWidget(self.input_numero)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(13, 24))
        self.label_12.setMaximumSize(QtCore.QSize(13, 24))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.input_uf = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_uf.setMinimumSize(QtCore.QSize(41, 24))
        self.input_uf.setMaximumSize(QtCore.QSize(41, 24))
        self.input_uf.setObjectName("input_uf")
        self.horizontalLayout_4.addWidget(self.input_uf)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.input_bairro = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_bairro.setMinimumSize(QtCore.QSize(261, 24))
        self.input_bairro.setMaximumSize(QtCore.QSize(261, 24))
        self.input_bairro.setObjectName("input_bairro")
        self.horizontalLayout_2.addWidget(self.input_bairro)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(33, 13))
        self.label_11.setMaximumSize(QtCore.QSize(33, 13))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.input_cidade = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_cidade.setMinimumSize(QtCore.QSize(261, 24))
        self.input_cidade.setMaximumSize(QtCore.QSize(261, 24))
        self.input_cidade.setObjectName("input_cidade")
        self.horizontalLayout_5.addWidget(self.input_cidade)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.inserir_dados)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Finalizar cadastro"))
        self.label.setText(_translate("Form", "Cadastro de Cliente"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.label_3.setText(_translate("Form", "Sobrenome"))
        self.label_4.setText(_translate("Form", "Data de nascimento"))
        self.label_5.setText(_translate("Form", "Telefone de contato"))
        self.label_6.setText(_translate("Form", "CPF"))
        self.label_7.setText(_translate("Form", "Endereço"))
        self.label_8.setText(_translate("Form", "Rua"))
        self.label_9.setText(_translate("Form", "Numero"))
        self.label_12.setText(_translate("Form", "UF"))
        self.label_10.setText(_translate("Form", "Bairro"))
        self.label_11.setText(_translate("Form", "Cidade"))

    def inserir_dados(self):

        try:
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
            
            self.clienteDAO.insert(cliente)
            QMessageBox.information(self.layoutWidget, 'Alerta', 'Sucesso ao cadastrar o Cliente.')
        except Exception as e:
            QMessageBox.critical(self.layoutWidget, 'Alerta', f'Error ao cadastrar o Cliente.')