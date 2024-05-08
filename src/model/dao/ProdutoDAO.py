from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Produto import Produto


class ProdutoDAO():

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(Produto).filter(Produto.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Produto).filter_by(id_produto=id, foi_deletado=False).first()

    def insert(self, produto: Produto):
        produto.foi_deletado = False
        try:
            self.session.add(produto)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir o Produto: \n{ex}")
            self.session.rollback()
            raise ex

    def update(self, produto: Produto):
        try:
            self.session.commit()
        except Exception as ex:
            print(f"Error ao alterar o Produto: \n{ex}")
            self.session.rollback()

    def delete(self, produto: Produto):
        try:
            produto.foi_deletado = True
            
            produto.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o produto: \n{ex}")
            self.session.rollback()
