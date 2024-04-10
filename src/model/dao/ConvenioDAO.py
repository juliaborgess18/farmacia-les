from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Convenio import Convenio

class ConvenioDAO:
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Convenio).all()
    
    def select_by_id(self, id: int):
        pass

    def insert(self, produto: Convenio):
        pass

    def update(self, produto: Convenio):
        pass

    def delete(self, produto: Convenio):
        pass