from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Cliente import Cliente

class ClienteDAO():

    def __init__(self, session):
        self.session = session
        
    def select_all(self):
        return self.session.query(Cliente).filter(Cliente.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Cliente).filter_by(id_cliente=id, foi_deletado=False).first()

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
            cliente.foi_deletado = True
            
            cliente.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o cliente: \n{ex}")
            self.session.rollback()
        
        