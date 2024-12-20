from app.services.interfaces import ABC, abstractmethod, List
from app.models import User

class UserServiceInterface(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass