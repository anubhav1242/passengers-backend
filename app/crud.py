from sqlalchemy.orm import Session
from models import Passengers
from schemas import PassengerSchema


def get_passengers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Passengers).offset(skip).limit(limit).all()


def get_passenger_by_id(db: Session, passenger_id: int):
    passenger = db.query(Passengers).filter(Passengers.id == passenger_id).first()
    print(passenger)
    return passenger

def create_passenger(db: Session, passengers: PassengerSchema):
    _passengers = Passengers(Survived=passengers.Survived, Pclass=passengers.Pclass, Name=passengers.Name, Sex=passengers.Sex, Age=passengers.Age, SibSp=passengers.SibSp, Parch=passengers.Parch, Ticket=passengers.Ticket, Fare=passengers.Fare, Cabin=passengers.Cabin, Embarked=passengers.Embarked)
    db.add(_passengers)
    db.commit()
    db.refresh(_passengers)
    return _passengers


def remove_passenger(db: Session, passenger_id: int):
    _passengers = get_passenger_by_id(db=db, passenger_id=passenger_id)
    db.delete(_passengers)
    db.commit()


def update_passenger(db: Session, passenger_id: int, Survived: bool, Pclass: int, Name: str, Sex: str, Age: float, SibSp: int, Parch: int, Ticket: str, Fare: float, Cabin: str, Embarked: str):
    _passengers = get_passenger_by_id(db=db, passenger_id=passenger_id)

    _passengers.Survived = Survived
    _passengers.Pclass = Pclass
    _passengers.Name = Name
    _passengers.Sex = Sex
    _passengers.Age = Age
    _passengers.SibSp = SibSp
    _passengers.Parch = Parch
    _passengers.Ticket = Ticket
    _passengers.Fare = Fare
    _passengers.Cabin = Cabin
    _passengers.Embarked = Embarked
    
    db.commit()
    db.refresh(_passengers)
    return _passengers