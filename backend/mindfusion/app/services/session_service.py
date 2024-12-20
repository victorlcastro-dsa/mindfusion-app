from app.services import List
from app.models import Session
from app.repositories.interfaces import SessionRepositoryInterface
from app.services.interfaces import SessionServiceInterface
from app.serializers import SessionSerializer
from app.utils import handle_service_errors, logger

class SessionService(SessionServiceInterface):
    def __init__(self, session_repository: SessionRepositoryInterface):
        self.session_repository = session_repository

    @handle_service_errors("SessionService")
    def get_all_sessions(self) -> List[SessionSerializer]:
        sessions = self.session_repository.get_all_sessions()
        return [SessionSerializer.from_orm(session) for session in sessions]

    @handle_service_errors("SessionService")
    def get_session_by_id(self, session_id: int) -> SessionSerializer:
        session = self.session_repository.get_session_by_id(session_id)
        if not session:
            logger.error(f"Session with ID {session_id} not found")
            raise ValueError(f"Session with ID {session_id} not found")
        return SessionSerializer.from_orm(session)

    @handle_service_errors("SessionService")
    def create_session(self, session: Session) -> SessionSerializer:
        created_session = self.session_repository.create_session(session)
        return SessionSerializer.from_orm(created_session)

    @handle_service_errors("SessionService")
    def update_session(self, session_id: int, session: Session) -> SessionSerializer:
        updated_session = self.session_repository.update_session(session_id, session)
        if not updated_session:
            logger.error(f"Session with ID {session_id} not found")
            raise ValueError(f"Session with ID {session_id} not found")
        return SessionSerializer.from_orm(updated_session)

    @handle_service_errors("SessionService")
    def delete_session(self, session_id: int) -> None:
        self.session_repository.delete_session(session_id)