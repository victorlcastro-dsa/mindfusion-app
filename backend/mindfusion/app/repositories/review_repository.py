from typing import List
from sqlalchemy.orm import Session
from app.models.review import Review
from app.repositories.interfaces import ReviewRepositoryInterface
from app.repositories import handle_repository_errors, _add_and_commit, _commit_and_refresh, logger

class ReviewRepository(ReviewRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    @handle_repository_errors("ReviewRepository")
    def get_all_reviews(self) -> List[Review]:
        """Retrieve all reviews from the database."""
        return self.db.query(Review).all()

    @handle_repository_errors("ReviewRepository")
    def get_review_by_id(self, review_id: int) -> Review:
        """Retrieve a review by its ID."""
        return self.db.query(Review).filter(Review.id == review_id).first()

    @handle_repository_errors("ReviewRepository")
    def create_review(self, review: Review) -> Review:
        """Create a new review in the database."""
        _add_and_commit(self.db, review)
        return review

    @handle_repository_errors("ReviewRepository")
    def update_review(self, review_id: int, review: Review) -> Review:
        """Update an existing review in the database."""
        db_review = self.get_review_by_id(review_id)
        if db_review:
            for key, value in review.dict().items():
                setattr(db_review, key, value)
            _commit_and_refresh(self.db, db_review)
        return db_review

    @handle_repository_errors("ReviewRepository")
    def delete_review(self, review_id: int) -> None:
        """Delete a review from the database."""
        db_review = self.get_review_by_id(review_id)
        if db_review:
            self.db.delete(db_review)
            self.db.commit()