from motor.motor_asyncio import AsyncIOMotorClient

from config.config import MONGO_DATABASE, MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

# database
database = client.get_database(MONGO_DATABASE)

# collections
files = database.get_collection("files")
