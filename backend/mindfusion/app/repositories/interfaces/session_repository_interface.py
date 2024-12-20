from abc import ABC, abstractmethod
from typing import List
from app.models.session import Session

class SessionRepositoryInterface(ABC):
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