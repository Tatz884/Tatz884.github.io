from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy import text

from typing import List, Tuple, Optional

import api.models.task as task_model
import api.schemas.task as task_schema


async def get_task(db: AsyncSession, user_key: str, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.user_key == user_key).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None 

async def update_task(
    db: AsyncSession, user_key: str, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    original.title = task_create.title
    original.user_key = user_key
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def create_task(
    db: AsyncSession, user_key: str, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    task.user_key = user_key
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks_with_done(db: AsyncSession, user_key: str) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).
            filter(task_model.Task.user_key == user_key).
            outerjoin(task_model.Done)
        )
    )
    return result.all()


async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()

# strategy 1 loop
# async def delete_all_tasks(db: AsyncSession, user_id: int) -> None:
#     rows = await db.execute(select(task_model.Task).filter(task_model.Task.user_id==user_id))
#     for row in rows.all():
#         await db.delete(row)
#     await db.commit()

# strategy 2 where
# async def delete_all_tasks(db: AsyncSession) -> None:    
#     await db.execute(
#         select(task_model.Task).where(task_model.Task.id==task_model.Task.id).delete()
#         )
#     db.commit()

# strategy 3 that works
# async def delete_all_tasks(db: AsyncSession, user_id: int) -> None:    
#     with open("./backend/api/cruds/delete_all_tasks.sql") as file:
#         query = text(file.read())
#         await db.execute(query)
#     await db.commit()