from app.services import List
from app.models import Review
from app.repositories.interfaces import ReviewRepositoryInterface
from app.services.interfaces import ReviewServiceInterface
from app.serializers import ReviewSerializer
from app.utils import handle_service_errors, logger

class ReviewService(ReviewServiceInterface):
    def __init__(self, review_repository: ReviewRepositoryInterface):
        self.review_repository = review_repository

    @handle_service_errors("ReviewService")
    def get_all_reviews(self) -> List[ReviewSerializer]:
        reviews = self.review_repository.get_all_reviews()
        return [ReviewSerializer.from_orm(review) for review in reviews]

    @handle_service_errors("ReviewService")
    def get_review_by_id(self, review_id: int) -> ReviewSerializer:
        review = self.review_repository.get_review_by_id(review_id)
        if not review:
            logger.error(f"Review with ID {review_id} not found")
            raise ValueError(f"Review with ID {review_id} not found")
        return ReviewSerializer.from_orm(review)

    @handle_service_errors("ReviewService")
    def create_review(self, review: Review) -> ReviewSerializer:
        created_review = self.review_repository.create_review(review)
        return ReviewSerializer.from_orm(created_review)

    @handle_service_errors("ReviewService")
    def update_review(self, review_id: int, review: Review) -> ReviewSerializer:
        updated_review = self.review_repository.update_review(review_id, review)
        if not updated_review:
            logger.error(f"Review with ID {review_id} not found")
            raise ValueError(f"Review with ID {review_id} not found")
        return ReviewSerializer.from_orm(updated_review)

    @handle_service_errors("ReviewService")
    def delete_review(self, review_id: int) -> None:
        self.review_repository.delete_review(review_id)