from pymongo import MongoClient
from utils.config import DATABASE_NAME
from dotenv import load_dotenv
import os

load_dotenv()

client =MongoClient(os.getenv('MONGO_URI'))

db = client[DATABASE_NAME]

def create_db():
    global user_collection
    user_collection=db["users"]
    
    global guild_collection
    guild_collection=db["guilds"]
    
    print(f"connected to the database:{DATABASE_NAME}")



