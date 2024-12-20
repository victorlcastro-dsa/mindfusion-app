from app.services.interfaces import ABC, abstractmethod, List
from app.models import Tutor

class TutorServiceInterface(ABC):
    @abstractmethod
    def get_all_tutors(self) -> List[Tutor]:
        pass

    @abstractmethod
    def get_tutor_by_id(self, tutor_id: int) -> Tutor:
        pass

    @abstractmethod
    def create_tutor(self, tutor: Tutor) -> Tutor:
        pass

    @abstractmethod
    def update_tutor(self, tutor_id: int, tutor: Tutor) -> Tutor:
        pass

    @abstractmethod
    def delete_tutor(self, tutor_id: int) -> None:
        pass