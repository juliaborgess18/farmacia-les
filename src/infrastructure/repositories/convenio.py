from datetime import date
from typing import List, Optional
import psycopg2
from sqlalchemy import and_, update

from infrastructure.config.database import get_db
from infrastructure.models.convenio import Convenio
from schemas.convenio import Convenio as ConvenioSchema
from util.mapper import Mapper

class ConvenioRepositorio:

    @classmethod
    def obter_todos(cls) -> Optional[List[Convenio]]:
        try:
            db = get_db()
            return db.query(Convenio).filter(Convenio.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return []
        
    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Convenio]:
        try:
            db = get_db()
            return db.query(Convenio).filter_by(id_convenio=id, foi_deletado=False).first()
        except Exception as e:
            print(e)    
            return None
        
    @classmethod
    def inserir(cls, convenio: Convenio) -> Optional[Convenio]:
        try:
            db = get_db()
            db.add(convenio)
            db.commit()
            db.refresh(convenio)
            return convenio
        except psycopg2.Error as ex:
            print(f"Error ao inserir o Convenio: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, convenio: Convenio):
        try:
            db = get_db()
            update_stmt = update(Convenio).where(Convenio.id_convenio == convenio.id_convenio).values(especialidade=convenio.especialidade,
                                                                                                      cnpj=convenio.cnpj)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o Convenio: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Convenio).where(Convenio.id_convenio == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o Convenio: \n{ex}")
            db.rollback()

    @classmethod
    def obter_com_filtros(cls, especialidade: str, data_inicio: date, data_final: date):
        try:
            db = get_db()
            filtro = and_(Convenio.foi_deletado == False,
                          Convenio.especialidade.like(f'%{especialidade}%'), 
                          Convenio.data_inicio_convenio >= data_inicio,
                          Convenio.data_inicio_convenio <= data_final)

            convenios = db.query(Convenio).filter(filtro).order_by(Convenio.especialidade).all()

            return convenios
        except Exception as ex:
            print(f"Error ao buscar o Produto: \n{ex}")
            return []