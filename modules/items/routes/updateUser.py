from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from modules.items.schema.schemas import UserUpdate, UserResponse
from modules.items.routes.createUser import users

router = APIRouter()

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    updated_data: UserUpdate,
    role: str = Query(...)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update users")

    for index, user in enumerate(users):
        if user.id == user_id:
            updated_user = UserResponse(
                id=user.id,
                username=updated_data.username or user.username,
                email=updated_data.email or user.email,
                role=updated_data.role or user.role,
                created_at=user.created_at,
                updated_at=datetime.now()
            )
            users[index] = updated_user
            return updated_user

    raise HTTPException(status_code=404, detail="User not found")
