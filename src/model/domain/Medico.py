import datetime
from model.domain.Endereco import Endereco
from model.domain.Pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, endereco: Endereco, data_nascimento: datetime, tel_contato, nome, sobrenome, id_medico):
        super().__init__(endereco, data_nascimento, tel_contato, nome, sobrenome, id_medico)
        self.data_inicio_convenio = None
        self.especialidade = ""
        self.cnpj = ""