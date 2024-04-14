from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Funcionario import Funcionario

class FuncionarioDAO():

    def __init__(self, session):
        self.session = session
        
    def select_all(self):
        return self.session.query(Funcionario).filter(Funcionario.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Funcionario).filter_by(id_fornecedor=id, foi_deletado=False).first()

    def insert(self, funcionario: Funcionario):
        pass

    def update(self, funcionario: Funcionario):
        pass

    def delete(self, funcionario: Funcionario):
        try:
            funcionario.foi_deletado = True
        
            funcionario.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o funcionario: \n{ex}")
            self.session.rollback()