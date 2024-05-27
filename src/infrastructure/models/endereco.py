from sqlalchemy import Column, Integer, String

from infrastructure.config.database import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    
    id_endereco = Column("idendereco",Integer, primary_key=True, autoincrement=True)
    rua = Column(String(45), nullable=False)
    numero = Column(Integer, nullable=False)
    bairro = Column(String(45), nullable=False)
    cidade = Column(String(45), nullable=False)
    uf = Column(String(2), nullable=False)