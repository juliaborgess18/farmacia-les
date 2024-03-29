import datetime
from model.domain.Endereco import Endereco
from model.domain.Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, endereco: Endereco, data_nascimento: datetime, tel_contato, nome, sobrenome, id_funcionario):
        super().__init__(endereco, data_nascimento, tel_contato, nome, sobrenome, id_funcionario)
        self.data_admissao = None
        self.funcao = ""
        self.esta_ativo = False
        self.salario = 0.0
        self.cpf = ""