from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.usuario import Usuario
from schemas.usuario import Usuario as UsuarioSchema
from util.mapper import Mapper

class UsuarioRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Usuario]]:
        try:
            db = get_db()
            return db.query(Usuario).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        try:
            db = get_db()
            return db.query(Usuario).filter_by(id_usuario=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return Usuario()

    @classmethod
    def inserir(cls, usuario: UsuarioSchema) -> Optional[Usuario]:
        usuario_db = Mapper.mapear_usuario(usuario)
        try:
            db = get_db()
            db.add(usuario_db)
            db.commit()
            db.refresh(usuario_db)
            return usuario_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o usuario: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, usuario: Usuario):
        try:
            db = get_db()
            update_stmt = update(Usuario).where(Usuario.id_usuario == usuario.id_usuario).values(nome_usuario=usuario.nome_usuario,
                                                                                                 senha_usuario=usuario.senha_usuario)
            db.execute(update_stmt)
            db.commit()
        except Exception as ex:
            print(f"Error ao alterar o usuario: \n{ex}")
            db.rollback()

    # Não implementado softdelete, por isso não funciona este método
    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Usuario).where(Usuario.id_usuario == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except Exception as ex:
            print(f"Error ao deletar o usuario: \n{ex}")
            db.rollback()



