from sqlalchemy import create_engine, engine,MetaData

engine=create_engine("mysql+pymysql://root:root@localhost:3306/test")
meta=MetaData()
conn=engine.connect()



