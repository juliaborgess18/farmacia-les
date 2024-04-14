from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Venda import Venda


class VendaDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Venda).filter(Venda.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Venda).filter(Venda.foi_deletado == False).get(id)

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