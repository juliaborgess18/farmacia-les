from datetime import date
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Convenio import Convenio

class ConvenioDAO:

    def __init__(self, session):
        self.session = session

    def select_all(self):
        return self.session.query(Convenio).filter(Convenio.foi_deletado == False).all()
    
    def select_by_id(self, id: int):
        return self.session.query(Convenio).filter_by(id_convenio=id, foi_deletado=False).first()
    
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
                convenio.foi_deletado = True
                
                convenio.data_delete = date.today()
                self.session.commit()
            except Exception as ex:
                print(f"Error ao deletar o convenio: \n{ex}")
                self.session.rollback()

    # def print_convenio():
    # print("========================")
    # print("======= Convênio =======")
    # dao = ConvenioDAO()
    # convenios = dao.select_all()

    # for convenio in convenios:
    #     print(f"Id do Convênio: {convenio.idconvenio}, Especialidade: {convenio.especialidade}, Data do início do convênio: {convenio.data_inicio_convenio}, CNPJ: {convenio.cnpj}, Id do Cliente: {convenio.cliente.idcliente}, Nome do Cliente: {convenio.cliente.nome} {convenio.cliente.sobrenome}")