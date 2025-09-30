from fastapi import APIRouter, HTTPException, Query
from modules.items.routes.createUser import users

router = APIRouter()

@router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int, role: str = Query(...)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete users")

    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": f"User {user_id} deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")
