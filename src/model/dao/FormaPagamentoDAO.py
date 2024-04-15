from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.FormaPagamento import FormaPagamento


class FormaPagamentoDAO():

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(FormaPagamento).all()


# def print_formaPagamento():
#     print("========================")
#     print("======== formaPagamento =======")
#     dao = FormaPagamentoDAO()
#     formaPagamento = dao.select_all()

#     for item in formaPagamento:
#         print(f"Id: {item.idformapagamento}, Nome: {item.nome}")