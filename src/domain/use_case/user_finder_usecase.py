from typing import Dict

from ..repositories.user_repository import UserRepository


class UserFinderUseCase:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def find(self, first_name: str) -> Dict:
        if not first_name.isalpha():
            raise ValueError('Invalid first name')

        if len(first_name) > 18:
            raise ValueError('First name too long')

        users = self.__user_repository.select_user(first_name)

        if users == []:
            raise ValueError('User not found')

        response = {
            'type': "Users",
            'count': len(users),
            "attributes": users
        }

        return response
