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
        return self.session.query(Cliente).get(id)

    def insert(self, cliente: Cliente):
        try:
            self.session.add(cliente)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir o cliente: \n{ex}")
            self.session.rollback()

    def update(self, cliente: Cliente):
        try:
            self.session.commit()
        except Exception as ex:
            print(f"Error ao alterar o cliente: \n{ex}")
            self.session.rollback()

    def delete(self, cliente: Cliente):
        try:
            self.session.delete(cliente.endereco)
            self.session.delete(cliente)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o cliente: \n{ex}")
            self.session.rollback()
        
        