from sqlalchemy import Boolean, Column, Double, ForeignKey, Integer, Date, String
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base
from infrastructure.models.formaPagamento import FormaPagamento
from infrastructure.models.cliente import Cliente
from infrastructure.models.funcionario import Funcionario
from infrastructure.models.itemVenda import ItemVenda

class Venda(Base):
    __tablename__ = 'venda'

    id_venda = Column("idvenda", Integer, primary_key=True, autoincrement=True)
    data_venda = Column("datavenda", Date, nullable=False)
    valor_total = Column("valortotal", Double, nullable=False)
    status = Column("status", String(45), nullable=False)
    itens_venda = relationship("ItemVenda", back_populates="venda")
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    # relacionamentos
    id_funcionario = Column("idfuncionario", Integer, ForeignKey('funcionario.idfuncionario'), nullable=False)
    funcionario = relationship("Funcionario")
    id_cliente = Column("idcliente", Integer, ForeignKey('cliente.idcliente'), nullable=False)
    cliente = relationship("Cliente")
    id_formapagamento = Column("idformapagamento", Integer, ForeignKey('formapagamento.idformapagamento'), nullable=False)
    forma_pagamento = relationship("FormaPagamento")