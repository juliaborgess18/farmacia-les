import datetime
from model.domain.Endereco import Endereco
from model.domain.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, endereco: Endereco, data_nascimento: datetime, tel_contato, nome, sobrenome, id_cliente, data_cadastro, cpf):
        super().__init__(endereco, data_nascimento, tel_contato, nome, sobrenome)
        self.id_cliente = id_cliente
        self.data_cadastro = data_cadastro
        self.cpf = cpf

