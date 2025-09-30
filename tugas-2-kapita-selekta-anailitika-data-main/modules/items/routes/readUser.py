from fastapi import APIRouter, HTTPException
from typing import List
from modules.items.schema.schemas import UserResponse
from modules.items.routes.createUser import users

router = APIRouter()

# READ ALL → hanya admin
@router.get("/", response_model=List[UserResponse])
def get_users(role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can view all users")
    return users

# READ BY ID → admin boleh siapa saja, staff hanya dirinya sendiri
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, role: str):
    for user in users:
        if user.id == user_id:
            # admin boleh ambil siapa saja
            if role == "admin":
                return user
            # staff hanya boleh ambil datanya sendiri
            if role == "staff" and user.role == "staff":
                return user
            raise HTTPException(status_code=403, detail="Staff can only view their own data")
    raise HTTPException(status_code=404, detail="User not found")
