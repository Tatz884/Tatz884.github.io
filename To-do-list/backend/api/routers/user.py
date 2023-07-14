from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import backend.api.schemas.user as user_schema
import backend.api.cruds.user as user_crud
from backend.api.db import get_db

router = APIRouter()

# # get all users
# @router.get("/users", response_model= List[user_schema.User])
# async def get_all_users(db: AsyncSession = Depends(get_db)):
#     return await user_crud.get_all_users(db)

# get an user data by key
@router.get("/users", response_model= user_schema.User)
async def get_user_by_key(user: user_schema.UserCreateRead, db: AsyncSession = Depends(get_db)):
    db_user = await user_crud.get_user_by_key(db, user_key=user.user_key)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await db_user

# create an user data
@router.post("/users", response_model=user_schema.UserCreateRead)
async def create_user(user: user_schema.UserCreateRead, db: AsyncSession = Depends(get_db)):
    # db_user = user_crud.get_user_by_key(db, user_key=user.key)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="User already existed")
    return await user_crud.create_user(db=db, user_create=user)

# delete a user by key
@router.delete("/users", response_model= None)
async def delete_user(user: user_schema.UserCreateRead, db: AsyncSession = Depends(get_db)):
    db_user = await user_crud.get_user_by_key(db, user_key=user.user_key)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await user_crud.delete_user(db=db, user=db_user)

# delete all users
@router.delete("/users", response_model= None)
async def delete_all_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.delete_all_users(db=db)

# @router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
# async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
#     done = await done_crud.get_done(db, task_id=task_id)
#     if done is not None:
#         raise HTTPException(status_code=400, detail="Done already exists")

#     return await done_crud.create_done(db, task_id)


# @router.delete("/tasks/{task_id}/done", response_model=None)
# async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
#     done = await done_crud.get_done(db, task_id=task_id)
#     if done is None:
#         raise HTTPException(status_code=404, detail="Done not found")

#     return await done_crud.delete_done(db, original=done)