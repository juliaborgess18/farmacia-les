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
        return self.session.query(Venda).all()

# def print_venda():
#     print("========================")
#     print("======== Venda =======")
#     dao = VendaDAO()
#     venda = dao.select_all()

#     for item in venda:
#         print(f"idvenda: {item.idvenda}, datavenda: {item.datavenda}, valortotal: {item.valortotal}, status: {item.status}, idformapagamento: {item.idformapagamento}, idfuncionario: {item.idfuncionario}, idcliente: {item.idcliente}")