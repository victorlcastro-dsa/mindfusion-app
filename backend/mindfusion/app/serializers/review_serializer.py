from app.serializers import BaseModel, Optional, datetime
from app.models import Review

class ReviewSerializer(BaseModel):
    id: int
    session_id: int
    student_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime

    @staticmethod
    def from_orm(review: Review) -> 'ReviewSerializer':
        return ReviewSerializer.from_orm(review)

    def to_dict(self) -> dict:
        return self.model_dump()

    @staticmethod
    def from_dict(data: dict) -> 'ReviewSerializer':
        return ReviewSerializer(**data)

    class Config:
        orm_mode = True