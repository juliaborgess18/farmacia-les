from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QWidget
from PyQt5.uic import loadUi

from model.dao.FornecedorDAO import FornecedorDAO
from model.dao.ProdutoDAO import ProdutoDAO
from model.domain.Produto import Produto
from model.database.BaseDAO import BaseDAO

class CadastroProdutoController(QWidget):

    session = BaseDAO.get_session()
    fornecedorDAO = FornecedorDAO(session)
    produtoDAO = ProdutoDAO(session)

    def __init__(self):
        super().__init__()
        loadUi('src/view/CadastroProdutoView.ui', self)
        self.btn_cadastrar_produto.clicked.connect(self.inserir_dados)
        self.carregar_tableWidget()
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
    
    def carregar_tableWidget(self):
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
        try:
            produto = Produto()
            
            produto.nome = self.input_nome.text()
            produto.valor = self.input_valor.text()
            produto.data_validade= self.input_data_validade.text()
            id_fornecedor = int(self.fornecedor_selecionado)  

            produto.fornecedor = self.fornecedorDAO.select_by_id(id_fornecedor)
            self.produtoDAO.insert(produto)
            QMessageBox.information(self.layoutWidget, 'Alerta', 'Sucesso ao cadastrar o Produto.')
        except Exception as e:
            QMessageBox.critical(self.layoutWidget, 'Alerta', f'Error ao cadastrar o Produto.')