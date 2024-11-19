import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class DatabaseSessionManager:
    def __init__(self):
        self.__connection_string = os.getenv(
            "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/clean_arch")
        self.__engine = self.__create_database_engine()
        self.__session = sessionmaker(bind=self.__engine)

    def __create_database_engine(self):
        try:
            engine = create_engine(self.__connection_string)
            return engine
        except SQLAlchemyError as e:
            print(f"Erro ao criar o engine do banco de dados: {e}")
            raise

    def get_engine(self) -> Engine:
        return self.__engine

    @contextmanager
    def create_session(self) -> Session:
        session = self.__session()
        try:
            yield session
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro durante a sessão do banco de dados: {e}")
            raise
        finally:
            session.close()
