from sqlalchemy import Boolean, Column, Date, Double, ForeignKey, Integer, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.Fornecedor import Fornecedor

class Produto(Base):
    __tablename__ = 'produto'

    id_produto = Column("idproduto", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    valor = Column("valor", Double, nullable=False)
    data_validade = Column("datavalidade", Date, nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)

    id_fornecedor = Column("idfornecedor",Integer, ForeignKey('fornecedor.idfornecedor'), nullable=False)

    fornecedor = relationship("Fornecedor")