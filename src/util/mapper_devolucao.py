from typing import List

from dto.devolucao.cadastrar_devolucao_dto import CadastrarDevolucaoDTO, ItemDevolucaoDTO
from dto.devolucao.editar_devolucao_dto import EditarDevolucaoDTO
from infrastructure.models.devolucao import Devolucao
from infrastructure.models.itemDevolucao import ItemDevolucao


class MapperDevolucao():

    @classmethod
    def mapear_itens_devolucao(cls, itens: List[ItemDevolucaoDTO]) -> List[ItemDevolucao]:
        retorno = []
        for item in itens:
            devolucao = ItemDevolucao(qtde=item.qtde, id_produto=item.id_produto)
            retorno.append(devolucao)
        return retorno

    @classmethod
    def mapear_cadastrar_devolucao_dto(cls, dto: CadastrarDevolucaoDTO) -> Devolucao:
        return Devolucao(
            id_venda = dto.id_venda,
            valor_devolucao = dto.valor_devolucao,
            itens_devolucao = cls.mapear_itens_devolucao(dto.itens_devolucao),
            data_delete=None,
            foi_deletado=False
        )
    
    @classmethod
    def mapear_editar_devolucao_dto(cls, dto: EditarDevolucaoDTO) -> ItemDevolucao:
        return ItemDevolucao(
            id_devolucao=dto.id_devolucao,
            id_produto=dto.id_produto,
            qtde=dto.qtde
        )