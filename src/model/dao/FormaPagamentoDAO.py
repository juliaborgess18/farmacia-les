from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.FormaPagamento import FormaPagamento


class FormaPagamentoDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(FormaPagamento).all()


# def print_formaPagamento():
#     print("========================")
#     print("======== formaPagamento =======")
#     dao = FormaPagamentoDAO()
#     formaPagamento = dao.select_all()

#     for item in formaPagamento:
#         print(f"Id: {item.idformapagamento}, Nome: {item.nome}")