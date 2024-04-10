from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from model.database.BaseORM import BaseORM, Base
from model.domain.Endereco import Endereco

class Cliente(Base):
    
    __tablename__ = 'cliente'  # Nome correto da tabela
    
    idcliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    sobrenome = Column(String(45), nullable=False)
    datanascimento = Column(Date, nullable=False)
    telcontato = Column(String(45), nullable=False)
    datacadastro = Column(Date, nullable=False)  # Alterado para Date
    cpf = Column(String(14), nullable=False, unique=True)
    idendereco = Column(Integer, ForeignKey('endereco.idendereco'), nullable=False)

    # Relacionamento com a tabela Endereco
    endereco = relationship("Endereco")

# # Cria uma sessão para interagir com o banco de dados
# Session = sessionmaker(bind=base_orm.engine)
# session = Session()

# # Exemplo de consulta SELECT para obter todos os campos da tabela Cliente
# clientes = session.query(Cliente).all()

# for cliente in clientes:
#     print(f'ID: {cliente.idcliente}, Nome: {cliente.nome}, Sobrenome: {cliente.sobrenome}, Data de Nascimento: {cliente.datanascimento}, Telefone de Contato: {cliente.telcontato}, Data de Cadastro: {cliente.datacadastro}, CPF: {cliente.cpf}, ID do Endereço: {cliente.idendereco}, RUA do Endereço: {cliente.endereco.rua}')

