from typing import List
from dto.venda.cadastrar_venda_dto import CadastrarItemVendaDTO, CadastrarVendaDTO
from infrastructure.models.venda import Venda
from infrastructure.models.itemVenda import ItemVenda   

class MapperVenda():
    
    @classmethod
    def mapear_itens_venda(cls, itens_venda: List[CadastrarItemVendaDTO]) -> List[ItemVenda]:
        itens_mapeados=[]
        for item in itens_venda:
            item_mapeado = ItemVenda(
                qtde=item.qtde,
                id_produto=item.id_produto,
                id_venda=item.id_venda
            )
            itens_mapeados.append(item_mapeado)
        return itens_mapeados

    @classmethod
    def mapear_venda(cls, venda: CadastrarVendaDTO) -> Venda:
        venda_mapeado = Venda(
            data_venda=venda.data_venda,
            valor_total=venda.valor_total,
            status=venda.status,
            data_delete=None,
            foi_deletado=False,
            id_funcionario=venda.id_funcionario,
            id_cliente=venda.id_cliente,
            id_formapagamento=venda.id_formapagamento,
            itens_venda=cls.mapear_itens_venda(venda.itens_venda)
        )
        return venda_mapeado