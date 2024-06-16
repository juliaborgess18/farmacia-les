from dto.funcionario.cadastrar_funcionario import CadastrarFuncionarioDTO
from infrastructure.models.funcionario import Funcionario as db_funcionario

from util.mapper_endereco import MapperEndereco

class MapperFuncionario:
    
    @classmethod
    def cadastrar_funcionario(cls, dto: CadastrarFuncionarioDTO) -> db_funcionario:
        funcionario_cadastrado = db_funcionario()
        
        funcionario_cadastrado.nome = dto.nome
        funcionario_cadastrado.sobrenome = dto.sobrenome
        funcionario_cadastrado.data_nascimento = dto.data_nascimento
        funcionario_cadastrado.tel_contato = dto.tel_contato
        funcionario_cadastrado.cpf = dto.cpf
        funcionario_cadastrado.data_admissao = dto.data_admissao
        funcionario_cadastrado.cargo = dto.cargo
        funcionario_cadastrado.salario = dto.salario
        
        funcionario_cadastrado.endereco = MapperEndereco.cadastrar_endereco(dto.endereco)
        
        funcionario_cadastrado.id_funcionario = None
        funcionario_cadastrado.id_endereco = None
        funcionario_cadastrado.esta_ativo = True
        funcionario_cadastrado.foi_deletado = False
        funcionario_cadastrado.data_delete = None
        
        return funcionario_cadastrado
        
        
        