# tests/test_user_endpoints.py
import pytest
from httpx import AsyncClient
from backend.main import create_app
from backend.db.database import connect_to_db, disconnect_from_db, create_tables

app = create_app()  # ensure this is a FastAPI instance

@pytest.fixture(scope="module", autouse=True)
async def setup_db():
    await connect_to_db()
    await create_tables()
    yield
    await disconnect_from_db()

@pytest.mark.asyncio
async def test_user_crud():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Create user
        response = await ac.post("/users", json={"name": "Alice", "email": "alice@example.com"})
        assert response.status_code == 200
        user_id = response.json()["id"]

        # Get user
        response = await ac.get(f"/users/{user_id}")
        assert response.status_code == 200

        # List users
        response = await ac.get("/users")
        assert response.status_code == 200
