from sqlalchemy import  Column, Integer, String, Boolean, Float
from config import Base

class Passengers(Base):
    __tablename__ ="passengers"

    id = Column(Integer, primary_key=True, index=True)
    Survived = Column(Boolean(), default = True)
    Pclass = Column(Integer)
    Name = Column(String, nullable = False)
    Sex = Column(String, nullable = False)
    Age = Column(Float)
    SibSp = Column(Integer)
    Parch = Column(Integer)
    Ticket = Column(String)
    Fare = Column(Float)
    Cabin = Column(String)
    Embarked = Column(String)