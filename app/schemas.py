from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

T = TypeVar('T')

Base = declarative_base()

class PassengerSchema(BaseModel):
    id: int = None
    Survived: Optional[bool] = None
    Pclass: Optional[int] = None
    Name: Optional[str] = None
    Sex: Optional[str] = None
    Age: Optional[float] = None
    SibSp: Optional[int] = None
    Parch: Optional[int] = None
    Ticket: Optional[str] = None
    Fare: Optional[float] = None
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None

    class Config:
        orm_mode = True

class Item(Base):
    __tablename__ = "passengers"
    id = Column(Integer, primary_key=True, index=True)
    Survived = Column(Boolean)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Float)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)

class ItemCreate(BaseModel):
    name: str
    description: str

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestPassenger(BaseModel):
    parameter: PassengerSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
