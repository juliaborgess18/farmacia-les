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
        return self.session.query(Convenio).get(id)

    def insert(self, convenio: Convenio):
        try:
            self.session.add(convenio)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao inserir o Convênio: \n{ex}")
            self.session.rollback()

    def update(self):
        try:
            # Sim, neste método apenas executamos o commit, qualquer alteração deve ser feita no objeto convênio que adiquirimos pelo método 'select_by_id', ao alterar qualquer campo deste objeto a função commit ira persistir no banco.
            self.session.commit()
        except Exception as ex:
            print(f"Error ao alterar o Convênio: \n{ex}")
            self.session.rollback()

    def delete(self, convenio: Convenio):
        try:
            self.session.delete(convenio)
            self.session.commit()
        except Exception as ex:
            print(f"Error ao deletar o Convênio: \n{ex}")
            self.session.rollback()

    # def print_convenio():
    # print("========================")
    # print("======= Convênio =======")
    # dao = ConvenioDAO()
    # convenios = dao.select_all()

    # for convenio in convenios:
    #     print(f"Id do Convênio: {convenio.idconvenio}, Especialidade: {convenio.especialidade}, Data do início do convênio: {convenio.data_inicio_convenio}, CNPJ: {convenio.cnpj}, Id do Cliente: {convenio.cliente.idcliente}, Nome do Cliente: {convenio.cliente.nome} {convenio.cliente.sobrenome}")