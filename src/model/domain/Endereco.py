from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import relationship
from sqlite3 import IntegrityError
from sqlalchemy.orm import sessionmaker
from model.database.BaseORM import BaseORM, Base

class EnderecoORM(Base):
    __tablename__ = 'endereco'
    idendereco = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    rua = Column(String(45), nullable=False)
    bairro = Column(String(45), nullable=False)
    cidade = Column(String(45), nullable=False)
    uf = Column(String(2), nullable=False)

class EnderecoDAO():
    session = ''
    def __init__(self):
        base_orm = BaseORM()
        self.session = sessionmaker(bind=base_orm.engine)
        Session = sessionmaker(bind=base_orm.engine)
        self.session = Session()

    #SELECT
    def select_all(self):
        return self.session.query(EnderecoORM).all()
    
    #INSERT
    def insert(self, endereco):
        try:
            self.session.add(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
    #UPDATE
    def update(self, endereco):
        try:
            self.session.merge(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
    #DELETE
    def delete(self, endereco):
        try:
            self.session.delete(endereco)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()

# SELECT
# enderecoDAO = EnderecoDAO()
# enderecos = enderecoDAO.select_all()
# for endereco in enderecos:
#     print(f'ID: {endereco.idendereco}, Numero: {endereco.numero}, Rua: {endereco.rua}, Bairro: {endereco.bairro}, Cidade: {endereco.cidade}, UF: {endereco.uf}')

#INSERT
# endereco_dao = EnderecoDAO()
# novo_endereco = EnderecoORM(numero=123, rua='Rua ABCS', bairro='Bairro B', cidade='Cidade C', uf='UF')

# endereco_dao.insert(novo_endereco)

#UPDATE
# Supondo que você já tenha instanciado a classe EnderecoDAO
# endereco_dao = EnderecoDAO()

# # Supondo que você queira atualizar o endereço com o ID 1
# endereco_para_atualizar = endereco_dao.session.query(EnderecoORM).filter_by(idendereco=1).first()

# if endereco_para_atualizar:
#     # Modifique os atributos conforme necessário
#     endereco_para_atualizar.numero = 456
#     endereco_para_atualizar.rua = 'Rua XYZ'
#     endereco_para_atualizar.bairro = 'Novo Bairro'
    
#     # Chame o método update para atualizar o endereço
#     endereco_dao.update(endereco_para_atualizar)
#     print("Endereço atualizado com sucesso!")
# else:
#     print("Endereço não encontrado.")
