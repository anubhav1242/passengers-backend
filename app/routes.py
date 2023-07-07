from fastapi import APIRouter, HTTPException, Path, Form, UploadFile
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PassengerSchema, Request, Response, RequestPassenger, ItemCreate, Item
from typing import Annotated
import crud
import csv
from models import Passengers

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_passenger_service(request: RequestPassenger, db: Session = Depends(get_db)):
    crud.create_passenger(db, passengers=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Passenger created successfully").dict(exclude_none=True)


@router.get('/{id}')
async def get_passenger_by_id(PassengerId: int, skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    print("Get passenger by id ", PassengerId)
    _passengers = crud.get_passenger_by_id(db, passenger_id=PassengerId)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_passengers)

@router.get("/")
async def get_passengers(skip: int = 0, limit: int = 500, db: Session = Depends(get_db)):
    _passengers = crud.get_passengers(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_passengers)


@router.put("/")
async def update_passenger(request: RequestPassenger, db: Session = Depends(get_db)):
    _passengers = crud.update_passenger(db, passenger_id=request.parameter.id, Survived=request.parameter.Survived, Pclass=request.parameter.Pclass, Name=request.parameter.Name, Sex=request.parameter.Sex, Age=request.parameter.Age, SibSp=request.parameter.SibSp, Parch=request.parameter.Parch, Ticket=request.parameter.Ticket, Fare=request.parameter.Fare, Cabin=request.parameter.Cabin, Embarked=request.parameter.Embarked)
    return Response(status="Ok", code="200", message="Success update data", result=_passengers)


@router.delete("/delete")
async def delete_passenger(request: RequestPassenger,  db: Session = Depends(get_db)):
    crud.remove_passenger(db, passenger_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


@router.post("/uploadfile/")
async def create_upload_file(csvfile: UploadFile | None = None):
    if csvfile.content_type == "text/csv":
        return Response(status="ok", code="200", message="Success upload file")
    else:
        return Response(status="Not ok", code="415", message="Please upload a csv file")
        
@router.post("/load_csv")
def load_csv(file: UploadFile, db: Session = Depends(get_db)):
    decoded_file = file.file.read().decode("utf-8").splitlines()

    reader = csv.DictReader(decoded_file)
    next(reader)
    data = list(next(reader))

    for row in data:
        record = Passengers(**row)
        db.add(record)

    db.commit()

    return {"message": "CSV data loaded successfully"}


@router.post("/upload")
async def upload_file(file: UploadFile | None = None):
    db = SessionLocal()

    contents = await file.read()
    lines = contents.decode().split("\n")

    # lines = [line for line in lines if line]

    for line in lines:
        columns = line.split(",")
        item = ItemCreate(id=columns[0], Survived=columns[1], Pclass=columns[2], Name=columns[3], Sex=columns[4], Age=columns[5], SibSp=columns[6], Parch=columns[7], Ticket=columns[8], Fare=columns[9], Cabin=columns[10], Embarked=columns[11])
        db_item = Item(**item.dict())
        db.add(db_item)

    db.commit()
    db.close()

    return {"message": "CSV file uploaded successfully"}