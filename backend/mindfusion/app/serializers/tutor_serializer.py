from app.serializers import BaseModel, Optional
from app.models import Tutor

class TutorSerializer(BaseModel):
    id: int
    specialization: str
    price_per_hour: float
    bio: Optional[str]
    availability: Optional[str]

    @staticmethod
    def from_orm(tutor: Tutor) -> 'TutorSerializer':
        return TutorSerializer.from_orm(tutor)

    def to_dict(self) -> dict:
        return self.model_dump()

    @staticmethod
    def from_dict(data: dict) -> 'TutorSerializer':
        return TutorSerializer(**data)

    class Config:
        orm_mode = True