from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import StudentAdmin
from schemas import StudentAdminCreate, StudentAdminUpdate, StudentAdminResponse

router = APIRouter(prefix="/studentadmins", tags=["Studentadmins"])

@router.get("/", response_model=List[StudentAdminResponse])
async def list_studentadmins(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(StudentAdmin).offset(skip).limit(limit)
    res = await db.execute(stmt)
    return res.scalars().all()

@router.post("/", response_model=StudentAdminResponse, status_code=status.HTTP_201_CREATED)
async def create_studentadmin(payload: StudentAdminCreate, db: AsyncSession = Depends(get_db)):
    record = StudentAdmin(**payload.model_dump())
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record

@router.get("/{studentadmin_id}", response_model=StudentAdminResponse)
async def get_studentadmin(studentadmin_id: int, db: AsyncSession = Depends(get_db)):
    record = await db.get(StudentAdmin, studentadmin_id)
    if not record:
        raise HTTPException(status_code=404, detail="StudentAdmin not found")
    return record

@router.put("/{studentadmin_id}", response_model=StudentAdminResponse)
async def update_studentadmin(studentadmin_id: int, payload: StudentAdminUpdate, db: AsyncSession = Depends(get_db)):
    record = await db.get(StudentAdmin, studentadmin_id)
    if not record:
        raise HTTPException(status_code=404, detail="StudentAdmin not found")
    for field, val in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, val)
    await db.commit()
    await db.refresh(record)
    return record

@router.delete("/{studentadmin_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_studentadmin(studentadmin_id: int, db: AsyncSession = Depends(get_db)):
    record = await db.get(StudentAdmin, studentadmin_id)
    if not record:
        raise HTTPException(status_code=404, detail="StudentAdmin not found")
    await db.delete(record)
    await db.commit()
