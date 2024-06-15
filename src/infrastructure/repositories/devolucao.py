from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import update
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
    def alterar(cls, devolucao: DevolucaoSchema):
        try:
            db = get_db()
            update_stmt = update(Devolucao).where(Devolucao.id_devolucao == devolucao.id_devolucao).values(valor_devolucao=devolucao.valor_devolucao)
            db.execute(update_stmt)

            for item in devolucao.itens_devolucao:
                item_update_stmt = update(ItemDevolucao).where(
                    ItemDevolucao.id_produto == item.id_produto,
                    ItemDevolucao.id_devolucao == devolucao.id_devolucao
                ).values(
                    qtde=item.qtde
                )
                db.execute(item_update_stmt)
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