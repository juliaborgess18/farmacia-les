from model.database.DatabasePostgreSQL import DatabasePostgreSQL as db
from sqlalchemy import Table, Column, MetaData, String, DateTime, Integer, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ClienteORM(Base):
    conexao = db()
    
    __tablename__ = 'cliente'

    metadata = MetaData()   
    nome = Column('nome', String),
    sobrenome = Column('sobrenome', String),
    data_nascimento = Column('datanascimento', DateTime),
    tel_contato = Column('telcontato', String),
    data_cadastro = Column('datacadastro', DateTime),
    cpf = Column('cpf', String),
    # id_endereco = Column('idendereco', String)
    
    table_cliente = Table(__tablename__, metadata,
                nome,
                sobrenome,
                data_nascimento,
                tel_contato,
                data_cadastro,
                cpf
                )
    
    def selecionar_clientes(self,):
        query = self.table_cliente.select()
        exe = self.conexao.abrir_conexao().execute(query)
        self.conexao.fechar_conexao()
        return exe.fetchall()

class EnderecoDAO(Base):
    __tablename__ = 'endereco'
    id_endereco = Column('idendereco',Integer, primary_key=True)
    numero = Column('numero', Integer)
    rua = Column('rua',String)
    bairro = Column('bairro', String)
    cidade = Column('cidade', String)
    uf = Column('uf', String)
    
    id_endereco = Column(Integer, ForeignKey('endereco.idendereco'))
    
    user = relationship("cliente", backref=backref('idendereco'))
 
    