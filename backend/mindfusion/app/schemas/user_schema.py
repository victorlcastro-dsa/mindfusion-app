from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    """Base schema for User."""
    email: EmailStr = Field(..., description="E-mail do usuário")
    role: str = Field(..., description="Tipo de usuário (student ou tutor)")

class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str = Field(..., min_length=8, description="Senha do usuário")

class UserUpdate(UserBase):
    """Schema for updating an existing user."""
    password: Optional[str] = Field(None, min_length=8, description="Nova senha do usuário")

class UserOut(UserBase):
    """Schema for outputting a user."""
    id: int = Field(..., description="ID do usuário")
    created_at: datetime = Field(..., description="Data de criação da conta")

    class Config:
        orm_mode = True