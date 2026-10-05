from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "mysql+mysqlconnector://root:swain%4012345@localhost:3306/login"
engine = create_engine(url)
session = sessionmaker(bind=engine, autoflush=True)
