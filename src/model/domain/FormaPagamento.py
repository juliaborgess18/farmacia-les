from sqlalchemy import Column, Date, ForeignKey, Integer, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship

class FormaPagamento(Base):
    __tablename__ = 'formapagamento'

    idformapagamento = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)