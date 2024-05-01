from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Usuario import Usuario

class UsuarioDAO():
    
    def __init__(self, session):
        self.session = session
        
    def verifica_usuario(self, usuario:Usuario) -> int:
        
        try:
            # Verifica se o usuário existe
            verifica_nome = self.session.query(Usuario).filter_by(nome_usuario=usuario.nome_usuario).first()
            verifica_senha = self.session.query(Usuario).filter_by(senha_usuario=usuario.senha_usuario).first()

            if verifica_nome and verifica_senha:
                # QMessageBox.information(self, 'Usuário encontrado', f'O usuário "{nome_usuario}" está cadastrado.')
                return 1
            else:
                # QMessageBox.warning(self, 'Usuário não encontrado', f'O usuário "{nome_usuario}" não está cadastrado.')
                return 0

        except Exception as e:
            # QMessageBox.critical(self, 'Erro', f'Ocorreu um erro: {str(e)}')
            # print(e)
            return 0
            