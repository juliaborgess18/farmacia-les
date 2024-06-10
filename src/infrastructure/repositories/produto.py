from datetime import date, datetime
from typing import List, Optional

from sqlalchemy import and_, update
from infrastructure.config.database import get_db
from infrastructure.models.produto import Produto
from schemas.produto import Produto as ProdutoSchema
from util.mapper import Mapper
from sqlalchemy import or_

class ProdutoRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Produto]]:
        try:
            db = get_db()
            return db.query(Produto).filter(Produto.foi_deletado == False).order_by(Produto.nome).all()
        except Exception as e:
            print(e)    
            return None
        
    @classmethod
    def obter_por_id(cls, id: int)-> Optional[Produto]:
        try:
            db = get_db()
            return db.query(Produto).filter_by(id_produto=id, foi_deletado=False).first()
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

    @classmethod
    def obter_com_filtros(cls, nome: str, data_inicio: date, data_final: date, valor_min: float, valor_max: float):
        try:
            db = get_db()
            filtro = and_(Produto.foi_deletado == False,
                          Produto.nome.like(f'%{nome}%'), 
                          Produto.data_validade >= (data_inicio if data_inicio is not None else date.min),
                          Produto.data_validade <= (data_final if data_final is not None else date.max),
                          Produto.valor >= (valor_min if valor_min is not None else 0),
                          Produto.valor <= (valor_max if valor_max is not None else float('inf'))
                          )

            produtos = db.query(Produto).filter(filtro).order_by(Produto.nome).all()

            return produtos
        except Exception as ex:
            print(f"Error ao buscar o Produto: \n{ex}")
            return []
