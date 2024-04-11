from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Cliente import Cliente

class ClienteDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def select_all(self):
        return self.session.query(Cliente).all()
    
    def select_by_id(self, id: int):
        pass

    def insert(self, cliente: Cliente):
        try:
            self.session.add(cliente)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir o cliente: \n{ex}")
            self.session.rollback()

    def update(self, cliente: Cliente):
        pass

    def delete(self, cliente: Cliente):
        pass
        
        