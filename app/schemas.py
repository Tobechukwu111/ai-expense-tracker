from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ExpenseCategory(str, Enum):
    food = "food"
    transport = "transport"
    utilities = "utilities"
    education = "education"
    miscellaneous = "miscellaneous"

class ExpenseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    merchant: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=100)
    category: ExpenseCategory
    amount: float = Field(gt=0)

class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    merchant: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None

class ExpenseDelete(BaseModel):
    id: str

class ExpenseOut(BaseModel):
    id: str
    title: str
    merchant: str
    description: str
    category: ExpenseCategory
    amount: float
    created_at: datetime