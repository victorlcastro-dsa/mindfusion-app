from pydantic import BaseModel, Field, conint
from typing import Optional
from datetime import datetime

class ReviewBase(BaseModel):
    """Base schema for Review."""
    session_id: int = Field(..., description="ID da sessão relacionada")
    student_id: int = Field(..., description="ID do estudante que fez a avaliação")
    rating: conint(ge=1, le=5) = Field(..., description="Avaliação de 1 a 5 estrelas")
    comment: Optional[str] = Field(None, max_length=500, description="Comentário opcional sobre a sessão")

class ReviewCreate(ReviewBase):
    """Schema for creating a new review."""
    pass

class ReviewUpdate(ReviewBase):
    """Schema for updating an existing review."""
    pass

class ReviewOut(ReviewBase):
    """Schema for outputting a review."""
    id: int = Field(..., description="ID da avaliação")
    created_at: datetime = Field(..., description="Data de criação da avaliação")

    class Config:
        orm_mode = True