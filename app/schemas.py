from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

T = TypeVar('T')

Base = declarative_base()

class PassengerSchema(BaseModel):
    id: int = None
    Survived: Optional[str] = None
    Pclass: Optional[str] = None
    Name: Optional[str] = None
    Sex: Optional[str] = None
    Age: Optional[str] = None
    SibSp: Optional[str] = None
    Parch: Optional[str] = None
    Ticket: Optional[str] = None
    Fare: Optional[str] = None
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestPassenger(BaseModel):
    parameter: PassengerSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
