from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


#Configure sua rota do Postgres 
#                         "postgresql://username:password@localhost/desafio"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/desafio"


engine = create_engine(SQLALCHEMY_DATABASE_URL) 
if not database_exists(engine.url):
    create_database(engine.url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()