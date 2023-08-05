from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from config import SessionLocal, engine
from sqlalchemy.orm import Session
from schemas import Response, RequestPassenger
import crud
import io
import pandas as pd


session = SessionLocal()

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


@router.post("/uploadcsv/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.StringIO((await file.read()).decode('utf-8')))
        df.to_sql('passengers3', engine, if_exists='append', index=False)
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=200, detail="Invalid CSV Format")