from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.task as task_schema
import api.cruds.task as task_crud
import api.cruds.user as user_crud
from api.db import get_db
router = APIRouter()


# @router.get("/users/", response_model=list{user_schema.User})
# async def list_tasks(db: AsyncSession = Depends(get_db)):
#     return await task_crud.get_tasks_with_done(db)


@router.get("/users/{user_key}/tasks", response_model=List[task_schema.Task])
async def list_tasks(user_key: str, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user_by_key(db, user_key)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await task_crud.get_tasks_with_done(db, user_key)


@router.post("/users/{user_key}/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    user_key: str, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, user_key, task_body)


@router.put("/users/{user_key}/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    user_key: str, task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, user_key, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, user_key, task_body, original=task,)


@router.delete("/users/{user_key}/tasks/{task_id}", response_model=None)
async def delete_task(user_key: str, task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, user_key, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)


# To be implemented....
# @router.delete("/users/{user_id}/tasks", response_model=None)
# async def delete_all_tasks(user_id: str, db: AsyncSession = Depends(get_db)):
#     # task = await task_crud.get_task(db, task_id=task_id)
#     # if task is None:
#     #     raise HTTPException(status_code=404, detail="Task not found")

#     return await task_crud.delete_all_tasks(db, user_id)


