from psycopg2 import IntegrityError
from model.database.BaseORM import BaseORM
from model.domain.Endereco import Endereco
from sqlalchemy.orm import sessionmaker

class EnderecoDAO():

    def __init__(self, session):
        self.session = session

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
