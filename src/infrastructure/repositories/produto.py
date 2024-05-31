from datetime import date
from typing import List, Optional

from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.produto import Produto
from schemas.produto import Produto as ProdutoSchema
from util.mapper import Mapper

class ProdutoRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Produto]]:
        try:
            db = get_db()
            return db.query(Produto).filter(Produto.foi_deletado == False).all()
        except Exception as e:
            print(e)    
            return None
        
    @classmethod
    def obter_por_id(cls, id: int)-> Optional[Produto]:
        try:
            db = get_db()
            return db.query(Produto).filter_by(id_produto=id).first()
        except Exception as e:
            print(e)    
            return None
        
    @classmethod
    def inserir(cls, produto: ProdutoSchema)-> Optional[Produto]:
        produto_db = Mapper.mapear_produto(produto)
        try:
            db = get_db()
            db.add(produto_db)
            db.commit()
            db.refresh(produto_db)
            return produto_db
        except Exception as ex:
            print(f"Error ao inserir o Produto: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, produto: ProdutoSchema):
        try:
            db = get_db()
            update_stmt = update(Produto).where(Produto.id_produto == produto.id_produto).values(nome=produto.nome,
                                                                                                 valor=produto.valor,
                                                                                                 data_validade=produto.data_validade,
                                                                                                 id_fornecedor=produto.id_fornecedor)
            db.execute(update_stmt)
            db.commit()
        except Exception as ex:
            print(f"Error ao alterar o Produto: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Produto).where(Produto.id_produto == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except Exception as ex:
            print(f"Error ao deletar o produto: \n{ex}")
            db.rollback()