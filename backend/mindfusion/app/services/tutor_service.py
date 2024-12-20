from app.services import List
from app.models import Tutor
from app.repositories.interfaces import TutorRepositoryInterface
from app.services.interfaces import TutorServiceInterface
from app.serializers import TutorSerializer
from app.utils import handle_service_errors, logger

class TutorService(TutorServiceInterface):
    def __init__(self, tutor_repository: TutorRepositoryInterface):
        self.tutor_repository = tutor_repository

    @handle_service_errors("TutorService")
    def get_all_tutors(self) -> List[TutorSerializer]:
        tutors = self.tutor_repository.get_all_tutors()
        return [TutorSerializer.from_orm(tutor) for tutor in tutors]

    @handle_service_errors("TutorService")
    def get_tutor_by_id(self, tutor_id: int) -> TutorSerializer:
        tutor = self.tutor_repository.get_tutor_by_id(tutor_id)
        if not tutor:
            logger.error(f"Tutor with ID {tutor_id} not found")
            raise ValueError(f"Tutor with ID {tutor_id} not found")
        return TutorSerializer.from_orm(tutor)

    @handle_service_errors("TutorService")
    def create_tutor(self, tutor: Tutor) -> TutorSerializer:
        created_tutor = self.tutor_repository.create_tutor(tutor)
        return TutorSerializer.from_orm(created_tutor)

    @handle_service_errors("TutorService")
    def update_tutor(self, tutor_id: int, tutor: Tutor) -> TutorSerializer:
        updated_tutor = self.tutor_repository.update_tutor(tutor_id, tutor)
        if not updated_tutor:
            logger.error(f"Tutor with ID {tutor_id} not found")
            raise ValueError(f"Tutor with ID {tutor_id} not found")
        return TutorSerializer.from_orm(updated_tutor)

    @handle_service_errors("TutorService")
    def delete_tutor(self, tutor_id: int) -> None:
        self.tutor_repository.delete_tutor(tutor_id)