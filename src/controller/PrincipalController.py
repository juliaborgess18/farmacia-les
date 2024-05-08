from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from controller.CadastroClienteController import CadastroClienteController
from controller.CadastroVendaController import CadastroVendaController
from controller.CadastroProdutoController import CadastroProdutoController
# Não remover o import abaixo, apesar da IDE acusar que ele não é utilizado, o PyQt5 está o utilizando para carregar os ícones da aplicação.
import resources_rc 
    
class openTelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('src/view/PrincipalView.ui', self)
        self.configureStackedWidget()
    
    def configureStackedWidget(self):
        # Crio os controllers 
        tela_venda = CadastroVendaController()
        tela_produto = CadastroProdutoController()
        tela_cliente = CadastroClienteController()

        # coloca em uma page
        self.page_vendas = tela_venda
        self.page_produto = tela_produto
        self.page_cliente = tela_cliente

        # coloca as pages no stackedWidget
        self.stackedWidget.addWidget(self.page_vendas)
        self.stackedWidget.addWidget(self.page_produto)
        self.stackedWidget.addWidget(self.page_cliente)

        # Conecta as pages com os botões
        self.btn_tela_inicio.clicked.connect(self.load_inicio)
        self.btn_tela_vendas.clicked.connect(self.loadVendas)
        self.btn_tela_produtos.clicked.connect(self.loadProdutos)
        self.btn_tela_clientes.clicked.connect(self.loadClientes)

    def load_inicio(self):
        self.stackedWidget.setCurrentIndex(0)

    def loadVendas(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def loadProdutos(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def loadClientes(self):
        self.stackedWidget.setCurrentIndex(3)
