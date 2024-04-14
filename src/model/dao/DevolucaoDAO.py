from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Devolucao import Devolucao

class DevolucaoDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Devolucao).filter(Devolucao.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Devolucao).filter(Devolucao.foi_deletado == False).get(id)

    def insert(self, devolucao: Devolucao):
        try:
            self.session.add(devolucao)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir a Devolucao: \n{ex}")
            self.session.rollback()

    def update(self, devolucao: Devolucao):
        try:
            self.session.commit()
        except Exception as ex:
            print(f"Error ao alterar a Devolucao: \n{ex}")
            self.session.rollback()

def delete(self, devolucao: Devolucao):
        try:
            devolucao.foi_deletado = True
            
            devolucao.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar a devolucao: \n{ex}")
            self.session.rollback()

    # def print_devolucao():
    # print("========================")
    # print("====== Devoluções ======")
    # dao = DevolucaoDAO()
    # devolucoes = dao.select_all()

    # for devolucao in devolucoes:
    #     print(f"Id: {devolucao.iddevolucao}, Valor: {devolucao.valor_devolucao}.")
    #     for item in devolucao.itens_devolucao:
    #         print(f"-> Id Produto: {item.idproduto}, Quantidade: {item.qtde}, Nome do Produto: {item.produto.nome}.")

    # def print_item_devolucao():
    #     print("========================")
    #     print("==== Item Devolução ====")

    #     engine = BaseORM.get_engine()
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #     items_devolucao = session.query(ItemDevolucao).all()

    #     for item in items_devolucao:
    #         print(f"Id Devolução: {item.iddevolucao}, Id Produto: {item.idproduto}, Quantidade: {item.qtde}, Nome do Produto: {item.produto.nome}, Valor da Devolução: {item.devolucao.valor_devolucao}")