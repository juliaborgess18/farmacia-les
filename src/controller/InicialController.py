from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from model.domain.Usuario import Usuario
from model.dao.UsuarioDAO import UsuarioDAO
from model.database.BaseDAO import BaseDAO
from controller.PrincipalController import openTelaPrincipal

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('src/view/InicialView.ui', self)
        self.button_entrar.clicked.connect(self.login)

    def login(self):
        session = BaseDAO.get_session()
        usuario_dao = UsuarioDAO(session)
        usuario = Usuario()
        
        usuario.nome_usuario = self.insert_nome_usuario.text()
        usuario.senha_usuario = self.insert_senha_usuario.text()
        
        if (usuario_dao.verifica_usuario(usuario) == 0):
            self.dados_invalidos.setText("Dados inválidos. Por gentileza, revise-os.")
        else:
            self.openMainWindow()

    def openMainWindow(self):
        self.mainWindow = openTelaPrincipal()
        self.mainWindow.setMinimumSize(1280, 720)
        self.mainWindow.setMaximumSize(1280, 720)
        self.mainWindow.show()
        self.close()