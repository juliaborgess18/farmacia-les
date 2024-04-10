from sqlalchemy import Column, Double, Integer
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship

class Devolucao(Base):
    __tablename__ = 'devolucao'

    iddevolucao = Column(Integer, primary_key=True, autoincrement=True)
    valor_devolucao = Column("valordevolucao", Double, nullable=False)
    itens_devolucao = relationship("ItemDevolucao", back_populates="devolucao")

    # devolucoes = session.query(Devolucao).all()
    # for devolucao in devolucoes:
    #     print(f"Id: {devolucao.iddevolucao}, Valor: {devolucao.valor_devolucao}")
    #     for item in devolucao.itens_devolucao:
    #         print(f"Id Produto: {item.idproduto}, Id Devolucao: {item.iddevolucao}, Nome do produto: {item.produto.nome}, Quantidade: {item.qtde}")