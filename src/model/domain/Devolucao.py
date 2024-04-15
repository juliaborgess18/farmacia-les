from sqlalchemy import Boolean, Column, Date, Double, Integer
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.ItemDevolucao import ItemDevolucao
from model.domain.Produto import Produto

class Devolucao(Base):
    __tablename__ = 'devolucao'

    id_devolucao = Column("iddevolucao", Integer, primary_key=True, autoincrement=True)
    valor_devolucao = Column("valordevolucao", Double, nullable=False)
    itens_devolucao = relationship("ItemDevolucao", back_populates="devolucao")
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
