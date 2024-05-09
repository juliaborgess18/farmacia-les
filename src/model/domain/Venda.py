from sqlalchemy import Boolean, Column, Double, ForeignKey, Integer, Date, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.FormaPagamento import FormaPagamento
from model.domain.Cliente import Cliente
from model.domain.Funcionario import Funcionario

class Venda(Base):
    __tablename__ = 'venda'

    id_venda = Column("idvenda", Integer, primary_key=True, autoincrement=True)
    data_venda = Column("datavenda", Date, nullable=False)
    valor_total = Column("valortotal", Double, nullable=False)
    status = Column("status", String(45), nullable=False)
    id_formapagamento = Column("idformapagamento", Integer, ForeignKey('formapagamento.idformapagamento'), nullable=False)
    id_funcionario = Column("idfuncionario", Integer, ForeignKey('funcionario.idfuncionario'), nullable=False)
    id_cliente = Column("idcliente", Integer, ForeignKey('cliente.idcliente'), nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    #teste
    item_venda = relationship("ItemVenda", back_populates="venda")
    
    funcionario = relationship("Funcionario")
    cliente = relationship("Cliente")
    forma_pagamento = relationship("FormaPagamento")