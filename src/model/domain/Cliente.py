from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from model.database.BaseORM import Base
from model.domain.Endereco import Endereco

class Cliente(Base):
    
    __tablename__ = 'cliente'  # Nome correto da tabela
    
    id_cliente = Column("idcliente",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String(45), nullable=False)
    sobrenome = Column("sobrenome",String(45), nullable=False)
    data_nascimento = Column("datanascimento",Date, nullable=False)
    tel_contato = Column("telcontato",String(45), nullable=False)
    data_cadastro = Column("datacadastro",Date, nullable=False)  # Alterado para Date
    cpf = Column("cpf",String(14), nullable=False, unique=True)
    id_endereco = Column("idendereco",Integer, ForeignKey('endereco.idendereco'), nullable=False)

    endereco = relationship("Endereco") # Relacionamento com a tabela Endereco

