from sqlalchemy import  Column, Integer, String
from config import Base
from pydantic import BaseModel

class Passengers(Base):
    __tablename__ ="passengers3"

    id = Column(Integer, primary_key=True, index=True)
    Survived = Column(String)
    Pclass = Column(String)
    Name = Column(String, nullable = False)
    Sex = Column(String, nullable = False)
    Age = Column(String)
    SibSp = Column(String)
    Parch = Column(String)
    Ticket = Column(String)
    Fare = Column(String)
    Cabin = Column(String)
    Embarked = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str