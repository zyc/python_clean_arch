from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnctionHandler:

    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql',
            'postgres',
            'postgres',
            'localhost',
            '5432',
            'clean_arch'
        )

        # self.__connection_string = "postgresql://postgres:postgres@localhost/clean_arch"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        maker = sessionmaker(bind=self.__engine)
        self.session = maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        # return self


# # sqli

# # default
# engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# # psycopg2
# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# # pg8000
# engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
