from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Transformar em variaveis de ambiente mais tarde
__username__ = 'postgres'
__password__ = 'postgres'
__hostname__ = '127.0.0.1:5432'
__database_name__ = 'farmacia-les'
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{__username__}:{__password__}@{__hostname__}/{__database_name__}'
#SQLALCHEMY_DATABASE_URL = "sqlite:///../app_farmacia.db" # Precisa inserir dados nesse banco

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10, 
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_bd():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    return db


