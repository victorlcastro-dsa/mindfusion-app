from app.services import List
from app.models import User
from app.repositories.interfaces import UserRepositoryInterface
from app.services.interfaces import UserServiceInterface
from app.serializers import UserSerializer
from app.utils import handle_service_errors, logger

class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    @handle_service_errors("UserService")
    def get_all_users(self) -> List[UserSerializer]:
        users = self.user_repository.get_all_users()
        return [UserSerializer.from_orm(user) for user in users]

    @handle_service_errors("UserService")
    def get_user_by_id(self, user_id: int) -> UserSerializer:
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            logger.error(f"User with ID {user_id} not found")
            raise ValueError(f"User with ID {user_id} not found")
        return UserSerializer.from_orm(user)

    @handle_service_errors("UserService")
    def create_user(self, user: User) -> UserSerializer:
        created_user = self.user_repository.create_user(user)
        return UserSerializer.from_orm(created_user)

    @handle_service_errors("UserService")
    def update_user(self, user_id: int, user: User) -> UserSerializer:
        updated_user = self.user_repository.update_user(user_id, user)
        if not updated_user:
            logger.error(f"User with ID {user_id} not found")
            raise ValueError(f"User with ID {user_id} not found")
        return UserSerializer.from_orm(updated_user)

    @handle_service_errors("UserService")
    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete_user(user_id)