from app.services.interfaces import ABC, abstractmethod, List
from app.models import Review

class ReviewServiceInterface(ABC):
    @abstractmethod
    def get_all_reviews(self) -> List[Review]:
        pass

    @abstractmethod
    def get_review_by_id(self, review_id: int) -> Review:
        pass

    @abstractmethod
    def create_review(self, review: Review) -> Review:
        pass

    @abstractmethod
    def update_review(self, review_id: int, review: Review) -> Review:
        pass

    @abstractmethod
    def delete_review(self, review_id: int) -> None:
        pass