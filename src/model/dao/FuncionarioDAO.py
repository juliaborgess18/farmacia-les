from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Funcionario import Funcionario

class FuncionarioDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def select_all(self):
        return self.session.query(Funcionario).all()
    
    def select_by_id(self, id: int):
        pass

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