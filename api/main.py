import os
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import pymysql
import pymysql.cursors

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")
MYSQL_URL = os.getenv("MYSQL_URL") 

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client.blog_db

def get_mysql_connection():
    return pymysql.connect(
        host='db_mysql',
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/posts")
async def get_posts():
    try:
        cursor = mongo_db.posts.find({}, {"_id": 0})
        posts = await cursor.to_list(length=100)
        return {"status": "OK", "data": posts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users")
def get_users():
    try:
        connection = get_mysql_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM utilisateurs")
            users = cursor.fetchall()
        connection.close()
        return {"status": "OK", "data": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))