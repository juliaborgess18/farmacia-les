from dto.cliente.cliente import AlterarClienteDTO, CadastrarClienteDTO
from infrastructure.models.cliente import Cliente as db
from util.mapper_endereco import MapperEndereco

class MapperCliente:
    
    @classmethod
    def cadastrar_cliente(cls, dto: CadastrarClienteDTO) -> db:
        cliente_cadastrado = db()
        
        cliente_cadastrado.id_cliente = dto.id_cliente
        cliente_cadastrado.nome = dto.nome
        cliente_cadastrado.sobrenome = dto.sobrenome
        cliente_cadastrado.data_nascimento = dto.data_nascimento
        cliente_cadastrado.tel_contato = dto.tel_contato
        cliente_cadastrado.cpf = dto.cpf
        
        cliente_cadastrado.endereco = MapperEndereco.cadastrar_endereco(dto.endereco)
        
        return cliente_cadastrado
        
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
        
        cliente_alterado.endereco = MapperEndereco.alterar_endereco(dto.endereco)
                        
        return cliente_alterado
    
        