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
# from controller.CadastroClienteController import Ui_Dialog
# from controller.CadastroProdutoController import Ui_Dialog
from controller.TelaInicialController import Ui_widget_login
# from controller.TelaPrincipalController import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    # TelaPrincipal.setMaximumSize(1024,728) # Definindo dimensões para congelar tela no 1024x728
    # TelaPrincipal.setMinimumSize(1024,728) # Definindo dimensões para congelar tela no 1024x728
    ui = Ui_MainWindow()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()