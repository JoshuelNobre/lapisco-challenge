from fastapi import FastAPI
from src.config import create_db
from src import user_router

create_db()

description = """
Simple CRUD developed for the LAPISCO challenge. 🚀

## User

* **Create users**.
* **Read all users**.
* **Read user**.
* **Update user**.
* **Delete user**.

"""
tags_metadata = [
    {
        "name": "user",
        "description": "Operations with users."
    }
]

app = FastAPI(title='CHALLENGE - LAPISCO - API',
    description=description,
    openapi_tags=tags_metadata)

# User route
app.include_router(user_router.router)