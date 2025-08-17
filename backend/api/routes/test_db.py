from fastapi import APIRouter
from backend.db.database import pool

router = APIRouter()

@router.get("/db-check")
async def db_check():
    async with pool.acquire() as connection:
        result = await connection.fetchval("SELECT 1;")
    return {"db_status": "connected", "test_result": result}
