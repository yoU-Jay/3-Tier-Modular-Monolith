from fastapi import APIRouter, Depends
from backend.models.user import User
from backend.services.user_service import UserService
from backend.db.database import get_db_pool  # your asyncpg pool setup

router = APIRouter()

# Dependency provider
def get_user_service():
    return UserService()

@router.post("/users", response_model=User, tags=["Users"])
async def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/users", response_model=list[User], tags=["Users"])
async def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.get("/test")
async def test_user_db():
    pool = await get_db_pool()  # get your connection pool
    async with pool.acquire() as conn:
        # Create table if it doesn't exist
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)
        # Insert a test user
        await conn.execute("""
            INSERT INTO users (name, email) VALUES ($1, $2)
        """, "Alice", "alice@example.com")

        # Fetch user
        user = await conn.fetchrow("SELECT * FROM users WHERE email=$1", "alice@example.com")

        # Optional: clean up after test
        await conn.execute("DROP TABLE users")

    return {"inserted_user": dict(user)}