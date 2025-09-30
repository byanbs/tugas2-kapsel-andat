from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from modules.items.schema.schemas import UserCreate, UserResponse, RoleEnum

router = APIRouter()
users: List[UserResponse] = []
id_counter = 1

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global id_counter
    new_user = UserResponse(
        id=id_counter,
        username=user.username,
        email=user.email,
        role=user.role,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    users.append(new_user)
    id_counter += 1
    return new_user

@router.get("/", response_model=List[UserResponse])
def get_all_users():
    return users
