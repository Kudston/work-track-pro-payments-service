"""Pydantic Models"""
from uuid import UUID
from typing import Optional
from sqlalchemy import Float, DateTime
from src.schemas import ParentPydanticModel

class WageOut(ParentPydanticModel):
    id: UUID
    task_id: UUID
    user_id: UUID
    total_hours: float
    total_amount: float

    date_created: DateTime
    date_updated: Optional[DateTime]

class ManyWagesOut(ParentPydanticModel):
    total: int
    wages: list[WageOut]

class TotalTaskWageAmount(ParentPydanticModel):
    total_amount: float
