from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Produto import Produto

class ProdutoDAO:
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Produto).filter(Produto.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Produto).filter(Produto.foi_deletado == False).get(id)

    def insert(self, produto: Produto):
        try:
            self.session.add(produto)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir o Produto: \n{ex}")
            self.session.rollback()

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

    # def print_produto():
    # print("========================")
    # print("======== Produto =======")
    # dao = ProdutoDAO()
    # produtos = dao.select_all()

    # for produto in produtos:
    #     print(f"Id: {produto.idproduto}, Nome: {produto.nome}, Valor: {produto.valor}, Data de Validade: {produto.data_validade}")