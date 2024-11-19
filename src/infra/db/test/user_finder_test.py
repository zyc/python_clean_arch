from src.data.use_case.user_finder import UserFinder
from src.infra.db.test.user_repository import UserRepositorySpy


def test_find():
    first_name = 'any_first_name 123'

    repo = UserRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)
