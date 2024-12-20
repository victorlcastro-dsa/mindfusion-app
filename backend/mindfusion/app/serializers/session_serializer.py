from app.serializers import BaseModel, datetime
from app.models import Session

class SessionSerializer(BaseModel):
    id: int
    tutor_id: int
    student_id: int
    scheduled_at: datetime
    status: str
    price: float

    @staticmethod
    def from_orm(session: Session) -> 'SessionSerializer':
        return SessionSerializer.from_orm(session)

    def to_dict(self) -> dict:
        return self.model_dump()

    @staticmethod
    def from_dict(data: dict) -> 'SessionSerializer':
        return SessionSerializer(**data)

    class Config:
        orm_mode = True