from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Convenio import Convenio

class ConvenioDAO:
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def select_all(self):
        return self.session.query(Convenio).all()
    
    def select_by_id(self, id: int):
        pass

    def insert(self, produto: Convenio):
        pass

    def update(self, produto: Convenio):
        pass

    def delete(self, produto: Convenio):
        pass

    # def print_convenio():
    # print("========================")
    # print("======= Convênio =======")
    # dao = ConvenioDAO()
    # convenios = dao.select_all()

    # for convenio in convenios:
    #     print(f"Id do Convênio: {convenio.idconvenio}, Especialidade: {convenio.especialidade}, Data do início do convênio: {convenio.data_inicio_convenio}, CNPJ: {convenio.cnpj}, Id do Cliente: {convenio.cliente.idcliente}, Nome do Cliente: {convenio.cliente.nome} {convenio.cliente.sobrenome}")