from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.Cliente import Cliente

class Convenio(Base):
    __tablename__ = 'convenio'

    id_convenio = Column("idconvenio", Integer, primary_key=True, autoincrement=True)
    especialidade = Column("especialidade", String(45), nullable=False)
    data_inicio_convenio = Column("datainicioconvenio", Date, nullable=False)
    cnpj = Column("cnpj", String(18), nullable=False)
    id_cliente = Column("idcliente", Integer, ForeignKey('cliente.idcliente'), nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    cliente = relationship("Cliente")


