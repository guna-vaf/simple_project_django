from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field

class StudentAdminBase(BaseModel):
    list_display: str
    search_fields: str
    list_filter: str

class StudentAdminCreate(StudentAdminBase):
    pass

class StudentAdminUpdate(BaseModel):
    list_display: Optional[str] = None
    search_fields: Optional[str] = None
    list_filter: Optional[str] = None

class StudentAdminResponse(StudentAdminBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    roll_number: str
    course: str
    age: int
    created_at: datetime
    updated_at: datetime

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    roll_number: Optional[str] = None
    course: Optional[str] = None
    age: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class StudentResponse(StudentBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
