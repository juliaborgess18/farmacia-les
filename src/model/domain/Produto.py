from sqlalchemy import Boolean, Column, Date, Double, Integer, String
from model.database.BaseORM import Base

class Produto(Base):
    __tablename__ = 'produto'

    id_produto = Column("idproduto", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    valor = Column("valor", Double, nullable=False)
    data_validade = Column("datavalidade", Date, nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
