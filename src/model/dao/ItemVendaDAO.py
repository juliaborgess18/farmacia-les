from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.ItemVenda import ItemVenda


class ItemVendaDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(ItemVenda).all()
    
# def print_itemVenda():
#     print("========================")
#     print("======== itemVenda =======")
#     dao =  ItemVendaDAO ()
#     ItemVenda = dao.select_all()

#     for item in ItemVenda:
#         print(f"qtde: {item.qtde}, idvenda: {item.idvenda}, idproduto: {item.idproduto}")