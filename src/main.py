''' Arquivo principal para executar o programa'''

from model.database.BaseORM import BaseORM, Base
from sqlalchemy.orm import sessionmaker
from model.domain.Funcionario import FuncionarioORM

base_orm = BaseORM()

if __name__ == "__main__":
    
    Session = sessionmaker(bind=base_orm.engine)
    session = Session()
    
    funcionarios = session.query(FuncionarioORM).all()

    for funcionario in funcionarios:
        print(f'{funcionario.idfuncionario}, {funcionario.nome}, {funcionario.sobrenome}, {funcionario.datanascimento}, {funcionario.telcontato}, {funcionario.dataadmissao}, {funcionario.cargo}, {funcionario.estaativo}, {funcionario.salario}, {funcionario.cpf}, {funcionario.endereco.rua}')
        
    