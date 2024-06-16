from dto.alterar_endereco import AlterarEnderecoDTO
from infrastructure.models.endereco import Endereco as db

class MapperEndereco:
    
    @classmethod 
    def alterar_endereco(cls, dto: AlterarEnderecoDTO) -> db:
        endereco_alterado = db() 
        
        endereco_alterado.rua = dto.rua
        endereco_alterado.numero = dto.numero
        endereco_alterado.bairro = dto.bairro
        endereco_alterado.cidade = dto.cidade
        endereco_alterado.uf = dto.uf 
              
        return endereco_alterado         
    