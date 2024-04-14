from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Venda import Venda

class VendaDAO():

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(Venda).filter(Venda.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Venda).filter_by(id_venda=id, foi_deletado=False).first()

    def insert(self, venda: Venda):
        pass

    def update(self, venda: Venda):
        pass
    
    def delete(self, venda: Venda):
        try:
            venda.foi_deletado = True
            
            venda.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar a venda: \n{ex}")
            self.session.rollback()

# def print_venda():
#     print("========================")
#     print("======== Venda =======")
#     dao = VendaDAO()
#     venda = dao.select_all()

#     for item in venda:
#         print(f"idvenda: {item.idvenda}, datavenda: {item.datavenda}, valortotal: {item.valortotal}, status: {item.status}, idformapagamento: {item.idformapagamento}, idfuncionario: {item.idfuncionario}, idcliente: {item.idcliente}")