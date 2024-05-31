from sqlalchemy import Boolean, Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.config.database import Base
from infrastructure.models.endereco import Endereco

class Funcionario(Base):
    __tablename__ = 'funcionario'
    
    id_funcionario = Column("idfuncionario",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(45), nullable=False)
    sobrenome = Column("sobrenome", String(45), nullable=False)
    data_nascimento = Column("datanascimento", Date, nullable=False)
    tel_contato = Column("telcontato", String(45), nullable=False)
    data_admissao = Column("dataadmissao", Date, nullable=False)
    cargo = Column(String(45), nullable=False)
    esta_ativo = Column("estaativo",Boolean, nullable=False)
    salario = Column("salario",Numeric, nullable=False)
    cpf = Column("cpf",String, nullable=False)
    # Soft Delete
    data_delete = Column("datadelete", Date)
    foi_deletado = Column("foideletado", Boolean)
    # relacionamentos
    id_endereco = Column("idendereco",Integer, ForeignKey('endereco.idendereco'), nullable=False)
    endereco = relationship("Endereco") 
