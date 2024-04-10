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