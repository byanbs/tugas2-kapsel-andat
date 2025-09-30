from fastapi import FastAPI
from modules.items.routes import createUser, readUser, updateUser, deleteUser

app = FastAPI(title="Users CRUD API")

# include routers
app.include_router(createUser.router, prefix="/users", tags=["users"])
app.include_router(readUser.router, prefix="/users", tags=["users"])
app.include_router(updateUser.router, prefix="/users", tags=["users"])
app.include_router(deleteUser.router, prefix="/users", tags=["users"])
