from typing import List
from sqlalchemy.orm import Session
from app.models.session import Session as SessionModel
from app.repositories.interfaces import SessionRepositoryInterface
from app.repositories import handle_repository_errors, _add_and_commit, _commit_and_refresh

class SessionRepository(SessionRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    @handle_repository_errors("SessionRepository")
    def get_all_sessions(self) -> List[SessionModel]:
        """Retrieve all sessions from the database."""
        return self.db.query(SessionModel).all()

    @handle_repository_errors("SessionRepository")
    def get_session_by_id(self, session_id: int) -> SessionModel:
        """Retrieve a session by its ID."""
        return self.db.query(SessionModel).filter(SessionModel.id == session_id).first()

    @handle_repository_errors("SessionRepository")
    def create_session(self, session: SessionModel) -> SessionModel:
        """Create a new session in the database."""
        _add_and_commit(self.db, session)
        return session

    @handle_repository_errors("SessionRepository")
    def update_session(self, session_id: int, session: SessionModel) -> SessionModel:
        """Update an existing session in the database."""
        db_session = self.get_session_by_id(session_id)
        if db_session:
            for key, value in session.dict().items():
                setattr(db_session, key, value)
            _commit_and_refresh(self.db, db_session)
        return db_session

    @handle_repository_errors("SessionRepository")
    def delete_session(self, session_id: int) -> None:
        """Delete a session from the database."""
        db_session = self.get_session_by_id(session_id)
        if db_session:
            self.db.delete(db_session)
            self.db.commit()