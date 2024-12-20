from pydantic import BaseModel, Field
from typing import Optional

class TutorBase(BaseModel):
    """Base schema for Tutor."""
    specialization: str = Field(..., description="Especialização do tutor")
    price_per_hour: float = Field(..., gt=0, description="Preço por hora da tutoria")
    bio: Optional[str] = Field(None, max_length=500, description="Biografia do tutor")
    availability: Optional[str] = Field(None, description="Disponibilidade do tutor")

class TutorCreate(TutorBase):
    """Schema for creating a new tutor."""
    pass

class TutorUpdate(TutorBase):
    """Schema for updating an existing tutor."""
    pass

class TutorOut(TutorBase):
    """Schema for outputting a tutor."""
    id: int = Field(..., description="ID do tutor")

    class Config:
        orm_mode = True