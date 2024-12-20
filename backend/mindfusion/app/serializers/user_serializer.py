from app.serializers import BaseModel, EmailStr, datetime
from app.models import User

class UserSerializer(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime

    @staticmethod
    def from_orm(user: User) -> 'UserSerializer':
        return UserSerializer.from_orm(user)

    def to_dict(self) -> dict:
        return self.model_dump()

    @staticmethod
    def from_dict(data: dict) -> 'UserSerializer':
        return UserSerializer(**data)

    class Config:
        orm_mode = True