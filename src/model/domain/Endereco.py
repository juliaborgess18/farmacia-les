from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import relationship
from sqlite3 import IntegrityError
from model.database.BaseORM import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    
    id_endereco = Column("idendereco",Integer, primary_key=True, autoincrement=True)
    rua = Column(String(45), nullable=False)
    numero = Column(Integer, nullable=False)
    bairro = Column(String(45), nullable=False)
    cidade = Column(String(45), nullable=False)
    uf = Column(String(2), nullable=False)