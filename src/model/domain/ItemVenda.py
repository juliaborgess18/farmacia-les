from model.database.BaseORM import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from model.domain.Venda import Venda
from model.domain.Produto import Produto

class ItemVenda(Base):
    __tablename__ = 'itemvenda'
    
    qtd = Column(Integer, nullable=False)
    id_venda = Column("idvenda", Integer, ForeignKey('venda.idvenda'), primary_key=True)
    id_produto = Column("idproduto", Integer, ForeignKey('produto.idproduto'), primary_key=True)

    venda = relationship("Venda")
    produto = relationship("Produto")