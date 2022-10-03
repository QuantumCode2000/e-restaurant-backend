from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()


@user.get("/users")
def find_all_users():
    return usersEntity(conn.local.user.find())


@user.post("/users")
def create_user(user: User):
    new_user = dict(user)
    id = conn.local.user.insert_one(new_user).inserted_id
    return str(id)


@user.get("/users/{user_id}")
def find_user():
    return


@user.put("/users/{user_id}/posts")
def update_user():
    return


@user.delete("/users/{user_id}")
def delete_user():
    return
