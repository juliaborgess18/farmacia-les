from psycopg2 import IntegrityError
from model.database.BaseORM import BaseORM
from model.domain.Endereco import Endereco
from sqlalchemy.orm import sessionmaker

class EnderecoDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    #SELECT
    def select_all(self):
        return self.session.query(Endereco).all()
    
    def select_all(self):
        return self.session.query(Endereco).all()
    
    def select_by_id(self, id: int):
        pass

    def insert(self, endereco: Endereco):
        pass

    def update(self, endereco: Endereco):
        pass

    def delete(self, endereco: Endereco):
        pass
