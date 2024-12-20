from pydantic import BaseModel, Field
from datetime import datetime

class SessionBase(BaseModel):
    """Base schema for Session."""
    tutor_id: int = Field(..., description="ID do tutor")
    student_id: int = Field(..., description="ID do estudante")
    scheduled_at: datetime = Field(..., description="Data e hora agendada para a sessão")
    status: str = Field(..., description="Status da sessão")
    price: float = Field(..., gt=0, description="Preço total da sessão")

class SessionCreate(SessionBase):
    """Schema for creating a new session."""
    pass

class SessionUpdate(SessionBase):
    """Schema for updating an existing session."""
    pass

class SessionOut(SessionBase):
    """Schema for outputting a session."""
    id: int = Field(..., description="ID da sessão")

    class Config:
        orm_mode = True