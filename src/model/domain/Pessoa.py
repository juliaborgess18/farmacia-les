import datetime
from model.domain.Endereco import Endereco

class Pessoa:
    def __init__(self, endereco: Endereco, data_nascimento: datetime, tel_contato="", nome="", sobrenome="", id_pessoa=0):
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.tel_contato = tel_contato
        self.nome = nome
        self.sobrenome = sobrenome
        self.id = id_pessoa
