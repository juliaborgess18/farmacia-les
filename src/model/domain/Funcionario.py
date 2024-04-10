from sqlalchemy import Boolean, Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from model.database.BaseORM import BaseORM, Base
from model.domain.Endereco import Endereco

base_orm = BaseORM()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    idfuncionario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    sobrenome = Column(String(45), nullable=False)
    datanascimento = Column(Date, nullable=False)
    telcontato = Column(String(45), nullable=False)
    dataadmissao = Column(Date, nullable=False)
    cargo = Column(String(45), nullable=False)
    estaativo = Column(Boolean, nullable=False)
    salario = Column(Numeric, nullable=False)
    cpf = Column(String, nullable=False)
    idendereco = Column(Integer, ForeignKey('endereco.idendereco'), nullable=False)

    # Relacionamento com a tabela Endereco
    endereco = relationship("Endereco")
