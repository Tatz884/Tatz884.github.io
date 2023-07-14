from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import backend.api.schemas.task as task_schema
import backend.api.schemas.user as user_schema
import backend.api.cruds.task as task_crud
from backend.api.db import get_db
router = APIRouter()


# @router.get("/users/", response_model=list{user_schema.User})
# async def list_tasks(db: AsyncSession = Depends(get_db)):
#     return await task_crud.get_tasks_with_done(db)


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(user: user_schema.UserCreateRead, db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db, user)


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
    user: user_schema.UserCreateRead, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, user, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    user: user_schema.UserCreateRead, task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, user, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(user: user_schema.UserCreateRead, task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, user, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)

@router.delete("/tasks", response_model=None)
async def delete_all_tasks(user: user_schema.UserCreateRead, db: AsyncSession = Depends(get_db)):
    # task = await task_crud.get_task(db, task_id=task_id)
    # if task is None:
    #     raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_all_tasks(user, db)


