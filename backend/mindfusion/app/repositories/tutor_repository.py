from typing import List
from sqlalchemy.orm import Session
from app.models.tutor import Tutor
from app.repositories.interfaces import TutorRepositoryInterface
from app.repositories import handle_repository_errors, _add_and_commit, _commit_and_refresh

class TutorRepository(TutorRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    @handle_repository_errors("TutorRepository")
    def get_all_tutors(self) -> List[Tutor]:
        """Retrieve all tutors from the database."""
        return self.db.query(Tutor).all()

    @handle_repository_errors("TutorRepository")
    def get_tutor_by_id(self, tutor_id: int) -> Tutor:
        """Retrieve a tutor by their ID."""
        return self.db.query(Tutor).filter(Tutor.id == tutor_id).first()

    @handle_repository_errors("TutorRepository")
    def create_tutor(self, tutor: Tutor) -> Tutor:
        """Create a new tutor in the database."""
        _add_and_commit(self.db, tutor)
        return tutor

    @handle_repository_errors("TutorRepository")
    def update_tutor(self, tutor_id: int, tutor: Tutor) -> Tutor:
        """Update an existing tutor in the database."""
        db_tutor = self.get_tutor_by_id(tutor_id)
        if db_tutor:
            for key, value in tutor.dict().items():
                setattr(db_tutor, key, value)
            _commit_and_refresh(self.db, db_tutor)
        return db_tutor

    @handle_repository_errors("TutorRepository")
    def delete_tutor(self, tutor_id: int) -> None:
        """Delete a tutor from the database."""
        db_tutor = self.get_tutor_by_id(tutor_id)
        if db_tutor:
            self.db.delete(db_tutor)
            self.db.commit()