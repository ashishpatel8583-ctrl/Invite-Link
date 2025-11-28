from motor.motor_asyncio import AsyncIOMotorClient

import os

MONGO_URI = os.getenv("mongodb+srv://bobbyutube48_db_user:er9RNl8mXVoJ3zlt@cluster0.akhtmm9.mongodb.net/?appName=Cluster0")
client = AsyncIOMotorClient(MONGO_URI)

db = client.Cluster0   # database name
tasks = db.tasks           # collection name
