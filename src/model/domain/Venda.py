from sqlalchemy import Column, Double, ForeignKey, Integer, Date, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.FormaPagamento import FormaPagamento
from model.domain.Cliente import Cliente
from model.domain.Funcionario import Funcionario

class Venda(Base):
    __tablename__ = 'venda'

    idvenda = Column(Integer, primary_key=True, autoincrement=True)
    datavenda = Column("datavenda", Date, nullable=False)
    valortotal = Column("valortotal", Double, nullable=False)
    status = Column("status", String(45), nullable=False)
    idformapagamento = Column(Integer, ForeignKey('formapagamento.idformapagamento'), nullable=False)
    idfuncionario = Column(Integer, ForeignKey('funcionario.idfuncionario'), nullable=False)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'), nullable=False)
    # Relacionamento com a tabela Endereco
    formapagamento = relationship("FormaPagamento")
    funcionario = relationship("Funcionario")
    cliente = relationship("Cliente")