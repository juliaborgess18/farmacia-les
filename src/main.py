''' Arquivo principal para executar o programa'''
import sys
from model.dao.ConvenioDAO import ConvenioDAO
from model.dao.DevolucaoDAO import DevolucaoDAO
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.ItemDevolucao import ItemDevolucao
from model.dao.ProdutoDAO import ProdutoDAO
from model.domain.Cliente import Cliente
from model.dao.ClienteDAO import ClienteDAO
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# from view.CadastroClienteController import Ui_Dialog
from view.CadastroProdutoController import Ui_Dialog

def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setMaximumSize(1024,728) # Definindo dimensões para congelar tela no 1024x728
    Dialog.setMinimumSize(1024,728) # Definindo dimensões para congelar tela no 1024x728
    Dialog.setWindowFlag(Qt.WindowMinimizeButtonHint, True) # Ativando o botão de minimizar
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    # clienteDAO.delete(clienteDAO.select_by_id(2))
    # clienteDAO = ClienteDAO()
    # result = clienteDAO.select_by_id(2)
    # result.nome = 'Systech'
    # clienteDAO.update(result)
    # print(result.nome)