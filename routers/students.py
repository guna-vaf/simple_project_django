from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/", response_model=List[StudentResponse])
async def list_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Student).offset(skip).limit(limit)
    res = await db.execute(stmt)
    return res.scalars().all()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(payload: StudentCreate, db: AsyncSession = Depends(get_db)):
    record = Student(**payload.model_dump())
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    record = await db.get(Student, student_id)
    if not record:
        raise HTTPException(status_code=404, detail="Student not found")
    return record

@router.put("/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, payload: StudentUpdate, db: AsyncSession = Depends(get_db)):
    record = await db.get(Student, student_id)
    if not record:
        raise HTTPException(status_code=404, detail="Student not found")
    for field, val in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, val)
    await db.commit()
    await db.refresh(record)
    return record

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    record = await db.get(Student, student_id)
    if not record:
        raise HTTPException(status_code=404, detail="Student not found")
    await db.delete(record)
    await db.commit()
