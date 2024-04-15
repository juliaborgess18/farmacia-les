from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.ItemVenda import ItemVenda

class ItemVendaDAO():

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(ItemVenda).all()
    
# def print_itemVenda():
#     print("========================")
#     print("======== itemVenda =======")
#     dao =  ItemVendaDAO ()
#     ItemVenda = dao.select_all()

#     for item in ItemVenda:
#         print(f"qtde: {item.qtde}, idvenda: {item.idvenda}, idproduto: {item.idproduto}")