from sqlalchemy import Column, Integer, String

from infrastructure.config.database import Base

class FormaPagamento(Base):
    __tablename__ = 'formapagamento'

    id_formapagamento = Column("idformapagamento", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)