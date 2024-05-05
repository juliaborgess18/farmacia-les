from PyQt5.QtWidgets import QMainWindow
from controller.CadastroClienteController import TelaCliente
from PyQt5.uic import loadUi
    
class openTelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carregue a interface .ui
        loadUi('src/view/PrincipalView.ui', self)
        self.configureStackedWidget()
    
    def configureStackedWidget(self):
        tela_vendas = TelaCliente()
        self.page_vendas = tela_vendas
        self.stackedWidget.addWidget(self.page_vendas)

        self.btn_tela_vendas.clicked.connect(self.loadVendas)
        self.btn_tela_produtos.clicked.connect(self.loadProdutos)
        self.btn_tela_clientes.clicked.connect(self.loadClientes)

    def loadVendas(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def loadProdutos(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def loadClientes(self):
        self.stackedWidget.setCurrentIndex(4)
