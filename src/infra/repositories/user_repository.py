from src.domain.models.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infra.db.entities.user_entity import UserEntity
from src.infra.db.session import DatabaseSessionManager


class UserSQLAlchemyRepository(UserRepository):

    def __init__(self, db_manager: DatabaseSessionManager):
        self.db_manager = db_manager

    def add(self, user: User) -> User:
        with self.db_manager.get_session() as session:
            entity = UserEntity(
                first_name=user.first_name,
                last_name=user.last_name,
                age=user.age
            )

            session.add(entity)
            session.commit()

    def get(self, user_id: int) -> User or None:
        with self.db_manager.get_session() as session:
            persisted = (
                session
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
