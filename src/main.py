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
from view.CadastroClienteController import Ui_Dialog

def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # main()
    clienteDAO = ClienteDAO()

    cliente_para_deletar = clienteDAO.select_by_id(1)
    clienteDAO.delete(cliente_para_deletar)
    result = clienteDAO.select_all()

    for item in result:
        print(f"Id: {item.id_cliente}, Nome: {item.nome}. ")

