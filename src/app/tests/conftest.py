from typing import AsyncGenerator
import pytest
from httpx import AsyncClient

from main import app


@pytest.fixture()
async def ac(scope="session") -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        yield ac
