from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Produto import Produto

class ProdutoDAO:
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Produto).all()
    
    def select_by_id(self, id: int):
        pass

    def insert(self, produto: Produto):
        pass

    def update(self, produto: Produto):
        pass

    def delete(self, produto: Produto):
        pass