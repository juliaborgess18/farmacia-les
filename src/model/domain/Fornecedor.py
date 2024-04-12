from sqlalchemy import Column, Date, ForeignKey, Integer, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.Endereco import Endereco

class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    idfornecedor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    cnpj = Column("cnpj", String(18), nullable=False)
    email = Column("email", String(45), nullable=False)
    telefone = Column("telefone", String(45), nullable=False)
    idendereco = Column(Integer, ForeignKey('endereco.idendereco'), nullable=False)
    # Relacionamento com a tabela Endereco
    endereco = relationship("Endereco")