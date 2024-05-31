from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base

class ItemVenda(Base):
    __tablename__ = 'itemvenda'
    
    qtde = Column(Integer, nullable=False)

    # relacionamentos
    id_produto = Column("idproduto", Integer, ForeignKey('produto.idproduto'), primary_key=True)
    produto = relationship("Produto")

    id_venda = Column("idvenda", Integer, ForeignKey('venda.idvenda'), primary_key=True)
    venda = relationship("Venda", back_populates="itens_venda", overlaps="itens_venda")
