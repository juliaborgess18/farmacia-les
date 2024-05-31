from datetime import date
from typing import List, Optional
import psycopg2
from sqlalchemy import update

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
            return db.query(Convenio).filter_by(id_convenio=id).first()
        except Exception as e:
            print(e)    
            return None
        
    @classmethod
    def inserir(cls, convenio: ConvenioSchema) -> Optional[Convenio]:
        convenio_db = Mapper.mapear_convenio(convenio)
        try:
            db = get_db()
            db.add(convenio_db)
            db.commit()
            db.refresh(convenio_db)
            return convenio_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o Convenio: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, convenio: ConvenioSchema):
        try:
            db = get_db()
            update_stmt = update(Convenio).where(Convenio.id_convenio == convenio.id_convenio).values(especialidade=convenio.especialidade,
                                                                                                      data_inicio_convenio=convenio.data_inicio_convenio,
                                                                                                      cnpj=convenio.cnpj,
                                                                                                      id_cliente = convenio.id_cliente)
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