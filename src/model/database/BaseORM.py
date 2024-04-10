from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseORM:

    @classmethod
    def get_engine(cls):
        __username__ = 'postgres'
        __password__ = 'root123'
        __hostname__ = '127.0.0.1:5432'
        __database_name__ = 'farmacia-les'
        engine = create_engine(f'postgresql+psycopg2://{__username__}:{__password__}@{__hostname__}/{__database_name__}')
        return engine