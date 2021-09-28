from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

@user.get("/api/")
async def read_data():
    return conn.execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()

@user.post("/api/addProfile/")
async def write_data(user:User):
    conn.execute(users.insert().values(
        name=user.first_name+" "+user.last_name,
        current_job=user.current_job,
        current_company=user.current_company,
        job_description=user.job_description,
        email=user.email
        
    ))
    return conn.execute(users.select()).fetchall()


@user.get("/api/getResumeByName/{name}")
async def read_data(name:str):
    print('=====',name)
    return conn.execute(users.select().where(users.c.name.contains(name))).fetchall()