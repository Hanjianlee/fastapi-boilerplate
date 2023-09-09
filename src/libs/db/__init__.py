from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

MYSQL_USERNAME = "username"
MYSQL_PASSWORD = "password"
MYSQL_HOST = "myslqhost"
MYSQL_PORT = 3306
MYSQL_DB_NAME = "dbname"

SQLALCHEMY_DATABSE_ASYNC_URL = (
    f"""mysql+asyncmy://{MYSQL_USERNAME}:{MYSQL_PASSWORD}"""
    + f"""@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"""
)

async_engine = create_async_engine(SQLALCHEMY_DATABSE_ASYNC_URL)

async_session_local = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_async_db():
    session: AsyncSession = async_session_local()
    try:
        yield session
        await session.commit()
    except Exception as ext:
        await session.rollback()
        raise ext
    finally:
        await session.close()
