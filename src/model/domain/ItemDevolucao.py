from model.database.BaseORM import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class ItemDevolucao(Base):
    __tablename__ = 'itemdevolucao'
    
    qtde = Column(Integer, nullable=False)
    id_produto = Column("idproduto", Integer, ForeignKey('produto.idproduto'), primary_key=True)
    id_devolucao = Column("iddevolucao", Integer, ForeignKey('devolucao.iddevolucao'), primary_key=True)

    produto = relationship("Produto")
    devolucao = relationship("Devolucao", back_populates="itens_devolucao", overlaps="itens_devolucao")
