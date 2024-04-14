from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Fornecedor import Fornecedor


class FornecedorDAO():

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(Fornecedor).filter(Fornecedor.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Fornecedor).filter_by(id_fornecedor=id, foi_deletado=False).first()

    def insert(self, fornecedor: Fornecedor):
        pass

    def update(self, fornecedor: Fornecedor):
        pass

    def delete(self, fornecedor: Fornecedor):
        try:
            fornecedor.foi_deletado = True
            
            fornecedor.data_delete = date.today()
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o fornecedor: \n{ex}")
            self.session.rollback()

    # def print_fornecedor():
    # print("========================")
    # print("======== fornecedor =======")
    # dao = FornecedorDAO()
    # fornecedor = dao.select_all()

    # for item in fornecedor:
    #     print(f"Id: {item.idfornecedor}, Nome: {item.nome}, Cnpj: {item.cnpj}, email: {item.email}, telefone: {item.telefone}, idendereco: {item.idendereco}")
    