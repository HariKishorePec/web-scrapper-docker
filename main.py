from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List
import database
import models
import schemas

app = FastAPI()

# Configure CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bulk_deals/", response_model=schemas.BulkDeals)
def create_bulk_deal(bulk_deal: schemas.BulkDealsCreate, db: Session = Depends(get_db)):
    try:
        db_bulk_deal = models.BulkDeals(**bulk_deal.dict())
        db.add(db_bulk_deal)
        db.commit()
        db.refresh(db_bulk_deal)
        return db_bulk_deal
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/bulk_deals/", response_model=List[schemas.BulkDeals])
def read_bulk_deals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bulk_deals = db.query(models.BulkDeals).offset(skip).limit(limit).all()
    return bulk_deals


@app.get("/bulk_deals/{bulk_deal_id}", response_model=schemas.BulkDeals)
def read_bulk_deal(bulk_deal_id: int, db: Session = Depends(get_db)):
    db_bulk_deal = db.query(models.BulkDeals).filter(
        models.BulkDeals.id == bulk_deal_id).first()
    if db_bulk_deal is None:
        raise HTTPException(status_code=404, detail="Bulk Deal not found")
    return db_bulk_deal


@app.put("/bulk_deals/{bulk_deal_id}", response_model=schemas.BulkDeals)
def update_bulk_deal(bulk_deal_id: int, bulk_deal: schemas.BulkDealsUpdate, db: Session = Depends(get_db)):
    try:
        db_bulk_deal = db.query(models.BulkDeals).filter(
            models.BulkDeals.id == bulk_deal_id).first()
        if db_bulk_deal is None:
            raise HTTPException(status_code=404, detail="Bulk Deal not found")
        for key, value in bulk_deal.dict(exclude_unset=True).items():
            setattr(db_bulk_deal, key, value)
        db.add(db_bulk_deal)
        db.commit()
        db.refresh(db_bulk_deal)
        return db_bulk_deal
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/bulk_deals/{bulk_deal_id}", response_model=schemas.BulkDeals)
def delete_bulk_deal(bulk_deal_id: int, db: Session = Depends(get_db)):
    db_bulk_deal = db.query(models.BulkDeals).filter(
        models.BulkDeals.id == bulk_deal_id).first()
    if db_bulk_deal is None:
        raise HTTPException(status_code=404, detail="Bulk Deal not found")
    db.delete(db_bulk_deal)
    db.commit()
    return db_bulk_deal
