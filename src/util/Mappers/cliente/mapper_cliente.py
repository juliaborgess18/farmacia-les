from dto.cliente.alterar_cliente import AlterarClienteDTO
from infrastructure.models.cliente import Cliente as db
from util.mapper_endereco import MapperEndereco

class MapperCliente:
    
    @classmethod
    def alterar_cliente(cls, dto: AlterarClienteDTO) -> db:
        cliente_alterado = db()
        
        cliente_alterado.id_cliente = dto.id_cliente
        cliente_alterado.nome = dto.nome
        cliente_alterado.sobrenome = dto.sobrenome
        cliente_alterado.data_nascimento = dto.data_nascimento
        cliente_alterado.cpf = dto.cpf
        cliente_alterado.tel_contato = dto.tel_contato
        cliente_alterado.data_cadastro = dto.data_cadastro
        
        cliente_alterado.id_endereco = dto.id_endereco
        cliente_alterado.endereco = MapperEndereco.alterar_endereco(dto.endereco)
                        
        return cliente_alterado