from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    staff = "staff"

class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=6,
        max_length=15,
        pattern=r'^[a-z0-9]+$',
        description="Lowercase alphanumeric only"
    )
    email: EmailStr
    role: RoleEnum

class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        description="8-20 chars, at least 1 uppercase, 1 lowercase, 1 digit, 1 special (! or @)"
    )

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        if not any(c in "!@" for c in v):
            raise ValueError("Password must contain at least one special character (! or @)")
        return v

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=6, max_length=15, pattern=r'^[a-z0-9]+$')
    email: Optional[EmailStr] = None
    role: Optional[RoleEnum] = None
    password: Optional[str] = Field(
        None,
        min_length=8,
        max_length=20,
        description="8-20 chars, at least 1 uppercase, 1 lowercase, 1 digit, 1 special (! or @)"
    )

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if v is None:
            return v
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        if not any(c in "!@" for c in v):
            raise ValueError("Password must contain at least one special character (! or @)")
        return v

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
