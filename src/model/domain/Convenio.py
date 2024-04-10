from sqlalchemy import Column, Date, ForeignKey, Integer, String
from model.database.BaseORM import Base
from sqlalchemy.orm import relationship
from model.domain.Cliente import Cliente

class Convenio(Base):
    __tablename__ = 'convenio'

    idconvenio = Column(Integer, primary_key=True, autoincrement=True)
    especialidade = Column("especialidade", String(45), nullable=False)
    data_inicio_convenio = Column("datainicioconvenio", Date, nullable=False)
    cnpj = Column("cnpj", String(18), nullable=False)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'), nullable=False)

    # Relacionamento com a tabela Endereco
    cliente = relationship("Cliente")


