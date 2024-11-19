from sqlalchemy.orm import Session

from ...domain.models.user import User
from ...domain.repositories.user_repository import UserRepository
from ..db.entities.user_entity import UserEntity


class UserSQLAlchemyRepository(UserRepository):

    def __init__(self, session: Session):
        self.__session = session

    def add(self, user: User) -> User:
        # with self.__db_manager.create_session() as session:
        entity = UserEntity(
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age
        )

        self.__session.add(entity)
        self.__session.commit()

    def get(self, user_id: int) -> User or None:
        # with self.__db_manager.create_session() as session:
        persisted = (
            self.__session
            .query(UserEntity)
            .filter(UserEntity.id == user_id)
            .first()
        )

        if not persisted:
            return None

        return User(
            user_id=persisted.id,
            first_name=persisted.first_name,
            last_name=persisted.last_name,
            age=persisted.age
        )
