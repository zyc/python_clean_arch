from abc import ABC, abstractmethod

from src.domain.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get(self, user_id: str) -> User:
        pass
