import uuid
from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from app.handlers.expenses import delete_expenses, get_expenses, create_expenses, update_expenses
from app.schemas import ExpenseCreate, ExpenseOut, ExpenseUpdate, ExpenseDelete
from app.storage import load_expenses, save_expenses

router = APIRouter(prefix="/api/v1/expenses", tags=["expenses"])

@router.get("/", response_model= list[ExpenseOut])
def expense_get():
    return get_expenses()

@router.post("/", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
def expense_create_routes(payload:ExpenseCreate):
    return create_expenses(payload)

@router.put("/", response_model=ExpenseOut)
def expense_update_routes(payload:ExpenseUpdate):
    return update_expenses(payload)


@router.delete("/", status_code = status.HTTP_204_NO_CONTENT)
def expense_delete_routes(payload:ExpenseDelete):
    return delete_expenses(payload)
