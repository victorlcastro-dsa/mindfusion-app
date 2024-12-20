from typing import List
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.interfaces import UserRepositoryInterface
from app.repositories import handle_repository_errors, _add_and_commit, _commit_and_refresh

class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    @handle_repository_errors("UserRepository")
    def get_all_users(self) -> List[User]:
        """Retrieve all users from the database."""
        return self.db.query(User).all()

    @handle_repository_errors("UserRepository")
    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve a user by their ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    @handle_repository_errors("UserRepository")
    def create_user(self, user: User) -> User:
        """Create a new user in the database."""
        self._add_and_commit(user)
        return user

    @handle_repository_errors("UserRepository")
    def update_user(self, user_id: int, user: User) -> User:
        """Update an existing user in the database."""
        db_user = self.get_user_by_id(user_id)
        if db_user:
            for key, value in user.dict().items():
                setattr(db_user, key, value)
            self._commit_and_refresh(db_user)
        return db_user

    @handle_repository_errors("UserRepository")
    def delete_user(self, user_id: int) -> None:
        """Delete a user from the database."""
        db_user = self.get_user_by_id(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()