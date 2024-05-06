from PyQt5.QtWidgets import QMainWindow, QPushButton
from controller.CadastroClienteController import TelaCliente
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile
    
class openTelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carregue a interface .ui
        loadUi('src/view/PrincipalView.ui', self)
        self.configureStackedWidget()
        # self.loadStyleSheet('src/view/css/estilo.css')
    
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
        self.btn_tela_clientes.setChecked(True)
        self.stackedWidget.setCurrentIndex(4)
        
    # def loadStyleSheet(self, file_name):
    # # Carrega o arquivo .css
    #     style_file = QFile(file_name)
    #     if not style_file.open(QFile.ReadOnly | QFile.Text):
    #         print("Erro ao abrir o arquivo de estilo:", style_file.errorString())
    #         return
    
    #     # Lê o conteúdo do arquivo
    #     style_sheet = style_file.readAll()
    #     style_file.close()
        
    #     # Aplica o estilo à interface
    #     self.btn_tela_clientes = False
    #     if self.btn_tela_clientes.isChecked():
    #         self.btn_tela_clientes.setStyleSheet(str(style_sheet, encoding='utf-8'))