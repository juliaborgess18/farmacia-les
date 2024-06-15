from datetime import date
from typing import Any, List, Optional

import psycopg2
from sqlalchemy import and_, update
from infrastructure.config.database import get_db
from infrastructure.models.devolucao import Devolucao
from infrastructure.models.itemDevolucao import ItemDevolucao
from schemas.devolucao import Devolucao as DevolucaoSchema
from util.mapper import Mapper

class DevolucaoRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Devolucao]]:
        try:
            db = get_db()
            return db.query(Devolucao).filter(Devolucao.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")       
            return []
        
    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Devolucao]:
        try:
            db = get_db()
            return db.query(Devolucao).filter_by(id_devolucao=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")          
            return Devolucao()
        
    @classmethod
    def inserir(cls, devolucao: Devolucao)-> Optional[Devolucao]:
        try:
            db = get_db()
            db.add(devolucao)
            db.commit()
            db.refresh(devolucao)
            return devolucao
        except psycopg2.Error as ex:
            print(f"Error ao inserir o Devolucao: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, devolucao: Devolucao):
        try:
            db = get_db()

            valor_total = 0
            for item in devolucao.itens_devolucao:
                item_update_stmt = update(ItemDevolucao).where(
                    ItemDevolucao.id_produto == item.id_produto,
                    ItemDevolucao.id_devolucao == devolucao.id_devolucao
                ).values(qtde=item.qtde)
                valor_total += item.qtde * item.produto.valor
                db.execute(item_update_stmt)
            update_stmt = update(Devolucao).where(Devolucao.id_devolucao == devolucao.id_devolucao).values(valor_devolucao=valor_total)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o Devolucao: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Devolucao).where(Devolucao.id_devolucao == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o devolucao: \n{ex}")
            db.rollback()

    @classmethod
    def obter_com_filtros(cls, id_venda: int, valor_min: float, valor_max: float):
        try:
            db = get_db()
            filtro = and_(Devolucao.foi_deletado == False,
                          Devolucao.valor_devolucao >= valor_min,
                          Devolucao.valor_devolucao <= valor_max
                         )
            if id_venda != None:
                filtro = and_(filtro, Devolucao.id_venda == id_venda)

            devolucao = db.query(Devolucao).filter(filtro).all()

            return devolucao
        except Exception as ex:
            print(f"Error ao buscar o Produto: \n{ex}")
            return []
        
    @classmethod
    def alterar_item_devolucao(cls, item_devolucao: ItemDevolucao):
        try:
            db = get_db()

            update_stmt = update(ItemDevolucao).where(ItemDevolucao.id_devolucao == item_devolucao.id_devolucao and ItemDevolucao.id_produto == item_devolucao.id_produto).values(qtde=item_devolucao.qtde)
            db.execute(update_stmt)

            devolucao = db.query(Devolucao).filter_by(id_devolucao=item_devolucao.id_devolucao).first()
            valor_total = 0
            for item in devolucao.itens_devolucao:
                valor_total += item.qtde * item.produto.valor

            devolucao.valor_devolucao = valor_total
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o Devolucao: \n{ex}")
            db.rollback()

