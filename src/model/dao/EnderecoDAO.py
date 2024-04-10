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
    
    #INSERT
    def insert(self, endereco):
        try:
            self.session.add(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
    #UPDATE
    def update(self, endereco):
        try:
            self.session.merge(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
    #DELETE
    def delete(self, endereco):
        try:
            self.session.delete(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
