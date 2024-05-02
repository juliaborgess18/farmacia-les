from sqlalchemy import Column, Integer, String
from model.database.BaseORM import Base


class Usuario(Base):
    __tablename__ = 'usuario'
    
    id_usuario = Column ("idusuario", Integer, primary_key=True)
    nome_usuario = Column("nomeusuario", String(100), nullable=False)
    senha_usuario = Column("senhausuario", String(8), nullable=False)