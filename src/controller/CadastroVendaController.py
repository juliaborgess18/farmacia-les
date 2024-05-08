from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class CadastroVendaController(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('src/view/CadastroVendaView.ui', self)
