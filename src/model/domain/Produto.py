from sqlalchemy import Column, Date, Double, Integer, String
from model.database.BaseORM import Base

class Produto(Base):
    __tablename__ = 'produto'

    idproduto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    valor = Column("valor", Double, nullable=False)
    data_validade = Column("datavalidade", Date, nullable=False)
