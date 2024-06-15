from datetime import date
from dto.convenio.cadastrar_convenio_dto import CadastrarConvenioDTO
from dto.convenio.editar_convenio_dto import EditarConvenioDTO
from infrastructure.models.convenio import Convenio


class MapperConvenio():
        
        @classmethod
        def mapear_cadastrar_convenio_dto(cls, dto: CadastrarConvenioDTO) -> Convenio: 
            return Convenio(
                especialidade=dto.especialidade,
                data_inicio_convenio=date.today(),
                cnpj=dto.cnpj,
                data_delete=None,
                foi_deletado=False,
                id_cliente = dto.id_cliente)
        
        @classmethod
        def mapear_editar_convenio_dto(cls, dto: EditarConvenioDTO) -> Convenio: 
            return Convenio(
                id_convenio=dto.id_convenio,
                especialidade=dto.especialidade,
                cnpj=dto.cnpj)