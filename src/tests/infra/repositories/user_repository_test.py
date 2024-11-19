import unittest

import pytest
from sqlalchemy import text

from ....domain.models.user import User
from ....infra.db.session import DatabaseSessionManager
from ....infra.repositories.user_repository import UserSQLAlchemyRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.__db_manager = DatabaseSessionManager()
        # self.repository = UserSQLAlchemyRepository(self.__db_manager)

    # def tearDown(self):
        # self.session.close()

    # @pytest.mark.skip(reason="This test is not ready yet")
    def test_add(self):
        with self.__db_manager.create_session() as session:
            user = User(
                user_id=0,
                first_name='any_first_name',
                last_name='any_last_name',
                age=30
            )

            repository = UserSQLAlchemyRepository(session)
            repository.add(user)

            sql = '''
                        select * from app_user
                        where first_name = '{}'
                        and last_name = '{}'
                        and age = {}
                '''.format(user.first_name, user.last_name, user.age)

            response = session.execute(text(sql))
            persisted = response.fetchone()

            assert persisted.first_name == user.first_name
            assert persisted.last_name == user.last_name
            assert persisted.age == user.age

            session.execute(
                text('delete from app_user where id = {}'.format(user.id)))
            # session.commit()

            print()
            print(user)

    def test_get(self):
        with self.__db_manager.create_session() as session:
            first_name = 'any_first_name_2'
            last_name = 'any_last_name_2'
            age = 30

            sql = '''
                    insert into app_user (first_name, last_name, age)
                        values ('{}', '{}', {})
                    returning id
            '''.format(first_name, last_name, age)

            result = session.execute(text(sql))
            generated_id = result.scalar()
            session.commit()

            repository = UserSQLAlchemyRepository(session)
            user = repository.get(generated_id)

            assert user.first_name == first_name
            assert user.last_name == last_name
            assert user.age == age

            print()
            print(user)

            session.execute(
                text('delete from app_user where id = {}'.format(user.id)))
            session.commit()
