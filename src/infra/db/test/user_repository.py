from typing import List

from src.domain.model.user import User


class UserRepositorySpy():

    def __init__(self):
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }

    def select_user(self, first_name: str) -> List[User]:
        self.select_user_attributes = {'first_name': first_name}

        return [
            User(
                user_id=1,
                first_name=first_name,
                last_name='sobrenome 1',
                age=20
            ),
            User(
                user_id=2,
                first_name=first_name,
                last_name='sobrenome 2',
                age=25
            )
        ]
