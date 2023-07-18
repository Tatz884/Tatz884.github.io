from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy import text
from sqlalchemy.orm import selectinload

from typing import List, Tuple, Optional

import api.models.task as task_model
import api.schemas.user as user_schema

# async def get_all_users(db: AsyncSession):
#     result: Result = await db.execute(
#         select(task_model.User)
#     )
#     # for a_user in result:
#     #     print("here I will print the result!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     #     print(a_user)
#     # users: str = str(result)
#     # users: Optional[Tuple[task_model.User]] = result.first()
#     return result if result is not None else None

async def get_user_by_id(db: AsyncSession, user_id: str) -> Optional[task_model.User]:
    result: Result = await db.execute(
        select(task_model.User).options(selectinload(task_model.User.tasks)).filter(task_model.User.id == user_id)
    )
    user: Optional[Tuple[task_model.User]] = result.first()
    return await user[0] if user is not None else None


async def get_user_by_key(db: AsyncSession, user_key: str) -> Optional[task_model.User]:
    result: Result = await db.execute(
        select(task_model.User).filter(task_model.User.user_key == user_key)
    )
    user: Optional[Tuple[task_model.User]] = result.first()
    return user[0] if user is not None else None

async def create_user(
    db: AsyncSession, user_create: user_schema.UserCreate
) -> task_model.User:
    user = task_model.User(**user_create.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user: task_model.User) -> None:
    await db.delete(user)
    await db.commit()

async def delete_all_users(db: AsyncSession) -> None:    
    with open("./backend/api/cruds/delete_all_users.sql") as file:
        query = text(file.read())
        await db.execute(query)
    await db.commit()