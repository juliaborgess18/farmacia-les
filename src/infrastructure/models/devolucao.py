from sqlalchemy import Boolean, Column, Date, Double, ForeignKey, Integer
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base
from infrastructure.models.produto import Produto
from infrastructure.models.itemDevolucao import ItemDevolucao

class Devolucao(Base):
    __tablename__ = 'devolucao'

    id_devolucao = Column("iddevolucao", Integer, primary_key=True, autoincrement=True)
    valor_devolucao = Column("valordevolucao", Double, nullable=False)
    itens_devolucao = relationship("ItemDevolucao", back_populates="devolucao")
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)

    # relacionamentos
    id_venda = Column("idvenda", Integer, ForeignKey('venda.idvenda'), nullable=False)
    venda = relationship("Venda")
