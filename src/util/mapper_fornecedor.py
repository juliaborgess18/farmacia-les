from dto.fornecedor.cadastrar_fornecedor_dto import CadastrarFornecedorDTO
from infrastructure.models.fornecedor import Fornecedor as db_fornecedor
from util.mapper_endereco import MapperEndereco

class MapperFornecedor:
    
    @classmethod
    def cadastrar_fornecedor(cls, dto: CadastrarFornecedorDTO) -> db_fornecedor:
        fornecedor_cadastrado = db_fornecedor()
        
        fornecedor_cadastrado.nome = dto.nome
        fornecedor_cadastrado.cnpj = dto.cnpj
        fornecedor_cadastrado.email = dto.email
        fornecedor_cadastrado.telefone = dto.telefone
        
        fornecedor_cadastrado.endereco = MapperEndereco.cadastrar_endereco(dto.endereco)
        
        fornecedor_cadastrado.id_fornecedor = None
        fornecedor_cadastrado.id_endereco = None
        fornecedor_cadastrado.esta_ativo = True
        fornecedor_cadastrado.foi_deletado = False
        fornecedor_cadastrado.data_delete = None
        
        return fornecedor_cadastrado
    
    # @classmethod 
    # def alterar_fornecedor(cls, dto: AlterarFornecedorDTO) -> db_fornecedor:
    #     fornecedor_alterado = db_fornecedor()

    #     fornecedor_alterado.id_fornecedor = dto.id_fornecedor
    #     fornecedor_alterado.nome = dto.nome
    #     fornecedor_alterado.cnpj = dto.cnpj
    #     fornecedor_alterado.email = dto.email
    #     fornecedor_alterado.telefone = dto.telefone
        
    #     fornecedor_alterado.endereco = MapperEndereco.alterar_endereco(dto.endereco)

    #     fornecedor_alterado.esta_ativo = True
    #     fornecedor_alterado.foi_deletado = False
    #     fornecedor_alterado.data_delete = None
        
    #     return fornecedor_alterado