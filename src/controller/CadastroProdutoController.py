# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/CadastroProdutoTeste.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QTableWidgetItem

from model.dao.FornecedorDAO import FornecedorDAO
from model.dao.ProdutoDAO import ProdutoDAO
from model.domain.Produto import Produto
from model.domain.Fornecedor import Fornecedor
from model.database.BaseDAO import BaseDAO

class Ui_Form(object):

    session = BaseDAO.get_session()
    fornecedorDAO = FornecedorDAO(session)
    produtoDAO = ProdutoDAO(session)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(762, 594)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 220, 261, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.input_valor = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_valor.setObjectName("input_valor")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_valor)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 341, 51))
        self.label.setStyleSheet("font: 75 24pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 110, 461, 61))
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 310, 461, 251))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_5.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.tableWidget = QtWidgets.QTableWidget(self.formLayoutWidget_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tableWidget)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(300, 220, 182, 59))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.input_data_validade = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.input_data_validade.setObjectName("input_data_validade")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_data_validade)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_4.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.inserir_dados)
        self.carregar_tableView()
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Valor"))
        self.label.setText(_translate("Form", "Cadastro de Produtos"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.pushButton.setText(_translate("Form", "Finalizar cadastro"))
        self.label_5.setText(_translate("Form", "Fornecedor"))
        self.label_4.setText(_translate("Form", "Data de Validade"))

    def carregar_tableView(self):
        headers = ('Id','Nome', 'CNPJ', 'Email', 'Telefone')
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setColumnWidth(0, 30)
        
        self.tableWidget.setHorizontalHeaderLabels(headers)

        fornecedores = self.fornecedorDAO.select_all()

        self.tableWidget.setRowCount(len(fornecedores))

        row_index = 0
        for item in fornecedores:
            self.tableWidget.setItem(row_index,0,QTableWidgetItem(str(item.id_fornecedor)))
            self.tableWidget.setItem(row_index,1,QTableWidgetItem(item.nome))
            self.tableWidget.setItem(row_index,2,QTableWidgetItem(item.cnpj))
            self.tableWidget.setItem(row_index,3,QTableWidgetItem(item.email))
            self.tableWidget.setItem(row_index,4,QTableWidgetItem(item.telefone))
            row_index += 1
    
    def on_cell_clicked(self, row, column):
        item = self.tableWidget.item(row, 0)

        if item is not None:
            self.fornecedor_selecionado = item.text()

    def inserir_dados(self):

        produto = Produto()
        
        produto.nome = self.input_nome.text()
        produto.valor = self.input_valor.text()
        produto.data_validade= self.input_data_validade.text()
        id_fornecedor = int(self.fornecedor_selecionado)  

        produto.fornecedor = self.fornecedorDAO.select_by_id(id_fornecedor)
        self.produtoDAO.insert(produto)
