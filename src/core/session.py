from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.core.settings import load_settings

engine = create_async_engine(load_settings().db_url, echo=True)
Base = declarative_base()

async_session = async_sessionmaker(engine, class_=AsyncSession,
                                   expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

