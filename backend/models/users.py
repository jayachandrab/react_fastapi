from sqlalchemy import Table,Column,MetaData
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta

users=Table(
    "users",meta,
    Column('id',Integer,primary_key=True),
     Column('name',String(255),primary_key=True),
      Column('current_job',String(255),primary_key=True),
      Column('job_description',String(255),primary_key=True),
      Column('current_company',String(255),primary_key=True),
      Column('email',String(255),primary_key=True),

)