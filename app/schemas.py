from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


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
    Cabin: Optional[float] = None
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
