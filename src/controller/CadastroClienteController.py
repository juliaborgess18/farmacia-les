from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from model.domain.Cliente import Cliente
from model.domain.Endereco import Endereco
from model.dao.ClienteDAO import ClienteDAO
from model.database.BaseDAO import BaseDAO

import datetime

class CadastroClienteController(QWidget):
    session = BaseDAO.get_session()
    clienteDAO = ClienteDAO(session)

    def __init__(self):
        super().__init__()
        loadUi('src/view/CadastroClienteView.ui', self)
        self.btn_cadastrar_cliente.clicked.connect(self.inserir_dados)
    
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
            print(e)
            QMessageBox.critical(self.layoutWidget, 'Alerta', f'Error ao cadastrar o Cliente.')