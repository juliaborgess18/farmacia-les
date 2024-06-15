from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.config.database import Base
from infrastructure.models.endereco import Endereco

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id_cliente = Column("idcliente",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String(45), nullable=False)
    sobrenome = Column("sobrenome",String(45), nullable=False)
    data_nascimento = Column("datanascimento",Date, nullable=False)
    tel_contato = Column("telcontato",String(45), nullable=False)
    data_cadastro = Column("datacadastro",Date, nullable=False) 
    cpf = Column("cpf",String(14), nullable=False, unique=True)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    # relacionamentos
    id_endereco = Column("idendereco",Integer, ForeignKey('endereco.idendereco'), nullable=False)
    endereco = relationship("Endereco")

