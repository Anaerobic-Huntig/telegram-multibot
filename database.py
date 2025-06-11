import asyncio
import aiosqlite
from pathlib import Path

DB_PATH = Path(__file__).parent / "bot.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS businesses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    name TEXT NOT NULL,
    biz_type TEXT NOT NULL,
    contact TEXT NOT NULL,
    start_code TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    business_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    image_url TEXT,
    FOREIGN KEY (business_id) REFERENCES businesses(id)
);
"""

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript(SCHEMA)
        await db.commit()

async def add_business(telegram_id: int, name: str, biz_type: str, contact: str, start_code: str):
    query = "INSERT INTO businesses (telegram_id, name, biz_type, contact, start_code) VALUES (?, ?, ?, ?, ?)"
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(query, (telegram_id, name, biz_type, contact, start_code))
        await db.commit()

async def get_business_by_code(code: str):
    query = "SELECT * FROM businesses WHERE start_code=?"
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(query, (code,)) as cursor:
            return await cursor.fetchone()

async def add_item(business_id: int, name: str, description: str, price: float, image_url: str | None = None):
    query = "INSERT INTO items (business_id, name, description, price, image_url) VALUES (?, ?, ?, ?, ?)"
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(query, (business_id, name, description, price, image_url))
        await db.commit()

async def get_items_for_business(business_id: int):
    query = "SELECT id, name, description, price, image_url FROM items WHERE business_id=?"
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(query, (business_id,)) as cursor:
            return await cursor.fetchall()

if __name__ == "__main__":
    asyncio.run(init_db())
