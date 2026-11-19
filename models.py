from datetime import datetime, date, timezone
from typing import Optional, List
from sqlalchemy import String, Integer, Boolean, Date, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class StudentAdmin(Base):
    __tablename__ = "studentadmins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    list_display: Mapped[str] = mapped_column(String(255), nullable=False)
    search_fields: Mapped[str] = mapped_column(String(255), nullable=False)
    list_filter: Mapped[str] = mapped_column(String(255), nullable=False)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    roll_number: Mapped[str] = mapped_column(String(255), nullable=False)
    course: Mapped[str] = mapped_column(String(255), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

