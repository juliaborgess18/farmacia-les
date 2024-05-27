from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.venda import Venda
from schemas.venda import Venda as VendaSchema
from util.mapper import Mapper

class VendaRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Venda]]:
        try:
            db = get_db()
            return db.query(Venda).filter(Venda.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao inserir o cliente: \n{ex}")    
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Venda]:
        try:
            db = get_db()
            return db.query(Venda).filter_by(id_venda=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao inserir o cliente: \n{ex}")    
            return Venda()

    @classmethod
    def inserir(cls, venda: VendaSchema) -> Optional[Venda]:
        venda_db = Mapper.mapear_venda(venda)
        try:
            db = get_db()
            db.add(venda_db)
            db.commit()
            db.refresh(venda_db)
            return venda_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o venda: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, venda: VendaSchema):
        try:
            db = get_db()
            update_stmt = update(Venda).where(Venda.id_venda == venda.id_venda).values(data_venda=venda.data_venda,
                                                                                       valor_total=venda.valor_total,
                                                                                       status=venda.status,
                                                                                       data_delete=None,
                                                                                       foi_deletado=False,
                                                                                       id_funcionario=venda.id_funcionario,
                                                                                       id_cliente=venda.id_cliente,
                                                                                       id_formapagamento=venda.id_formapagamento)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o cliente: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Venda).where(Venda.id_venda == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o venda: \n{ex}")
            db.rollback()



