from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://FullStackToDoApp_knownpair:741a23bc1f5556ffb05fcfd2e722458ad9a66bcb@6-u.h.filess.io:3307/FullStackToDoApp_knownpair"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session