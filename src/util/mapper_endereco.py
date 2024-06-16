from dto.endereco.endereco import AlterarEnderecoDTO, CadastrarEnderecoDTO
from infrastructure.models.endereco import Endereco as db

class MapperEndereco:
    
    @classmethod 
    def cadastrar_endereco(cls, dto: CadastrarEnderecoDTO) -> db:
        endereco_alterado = db() 
        
        endereco_alterado.rua = dto.rua
        endereco_alterado.numero = dto.numero
        endereco_alterado.bairro = dto.bairro
        endereco_alterado.cidade = dto.cidade
        endereco_alterado.uf = dto.uf 
              
        return endereco_alterado  
    
    @classmethod 
    def alterar_endereco(cls, dto: AlterarEnderecoDTO) -> db:
        endereco_alterado = db() 
        
        endereco_alterado.rua = dto.rua
        endereco_alterado.numero = dto.numero
        endereco_alterado.bairro = dto.bairro
        endereco_alterado.cidade = dto.cidade
        endereco_alterado.uf = dto.uf 
              
        return endereco_alterado    
    
         
    