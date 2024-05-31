from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base
from infrastructure.models.endereco import Endereco

class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    id_fornecedor = Column("idfornecedor", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    cnpj = Column("cnpj", String(18), nullable=False)
    email = Column("email", String(45), nullable=False)
    telefone = Column("telefone", String(45), nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    # relacionamentos
    id_endereco = Column("idendereco", Integer, ForeignKey('endereco.idendereco'), nullable=False)
    endereco = relationship("Endereco")