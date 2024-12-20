from app.services.interfaces import ABC, abstractmethod, List
from app.models import Session

class SessionServiceInterface(ABC):
    @abstractmethod
    def get_all_sessions(self) -> List[Session]:
        pass

    @abstractmethod
    def get_session_by_id(self, session_id: int) -> Session:
        pass

    @abstractmethod
    def create_session(self, session: Session) -> Session:
        pass

    @abstractmethod
    def update_session(self, session_id: int, session: Session) -> Session:
        pass

    @abstractmethod
    def delete_session(self, session_id: int) -> None:
        pass