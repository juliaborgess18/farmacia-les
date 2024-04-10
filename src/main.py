''' Arquivo principal para executar o programa'''

from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.Funcionario import Funcionario
from model.dao.FuncionarioDAO import FuncionarioDAO

base_orm = BaseORM()

if __name__ == "__main__":
    
    funcionarioDAO = FuncionarioDAO()
    funcionarios = funcionarioDAO.select_all()
    
    for funcionario in funcionarios:
        print(f'{funcionario.idfuncionario}, {funcionario.nome}, {funcionario.sobrenome}, {funcionario.datanascimento}, {funcionario.telcontato}, {funcionario.dataadmissao}, {funcionario.cargo}, {funcionario.estaativo}, {funcionario.salario}, {funcionario.cpf}, {funcionario.endereco.rua}')
        
    