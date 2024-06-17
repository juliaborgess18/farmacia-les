from typing import List
from dto.relatorios.relatorio_quantidade_produtos_vendidos import RelatorioQuantidadeProdutosVendidosDTO


class MapperRelatorios():
        
        @classmethod
        def mapear_relatorio_quantidade_produtos_vendidos(cls, relatorio) -> List[RelatorioQuantidadeProdutosVendidosDTO]: 
            relatorio_mapeado = []
            for item in relatorio:
                registro = RelatorioQuantidadeProdutosVendidosDTO(
                    id_produto = str(item[0]),
                    nome = item[1],
                    qtde = str(item[2]),
                    valor_unitario = str(item[3]),
                    valor_total = str(item[4]))
                relatorio_mapeado.append(registro)
            return relatorio_mapeado