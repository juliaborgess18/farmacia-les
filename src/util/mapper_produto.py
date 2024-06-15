from dto.produto.cadastrar_produto_dto import CadastrarProdutoDTO
from dto.produto.editar_produto_dto import EditarProdutoDTO
from infrastructure.models.produto import Produto


class MapperProduto():

        @classmethod
        def mapear_cadastrar_produto_dto(cls, dto: CadastrarProdutoDTO) -> Produto:
            return Produto(
                nome=dto.nome,
                valor=dto.valor,
                data_validade=dto.data_validade,
                id_fornecedor=dto.id_fornecedor,
                data_delete=None,
                foi_deletado=False
            )
        
        @classmethod
        def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
            return Produto(
                id_produto= dto.id_produto,
                nome=dto.nome,
                valor=dto.valor,
                data_validade=dto.data_validade
            )