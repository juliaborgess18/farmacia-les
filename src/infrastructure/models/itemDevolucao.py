from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base

class ItemDevolucao(Base):
    __tablename__ = 'itemdevolucao'
    
    qtde = Column(Integer, nullable=False)

    # relacionamentos
    id_produto = Column("idproduto", Integer, ForeignKey('produto.idproduto'), primary_key=True)
    produto = relationship("Produto")

    id_devolucao = Column("iddevolucao", Integer, ForeignKey('devolucao.iddevolucao'), primary_key=True)
    devolucao = relationship("Devolucao", back_populates="itens_devolucao", overlaps="itens_devolucao")
