import uuid
from fastapi import HTTPException
from datetime import datetime
from app.schemas import ExpenseCreate, ExpenseDelete, ExpenseUpdate, ExpenseOut
from app.storage import load_expenses, save_expenses

def get_expenses():
    expenses = load_expenses()
    return expenses


def delete_expenses(payload: ExpenseDelete):
    expenses = load_expenses()

    for idx, transaction in enumerate(expenses):
        if transaction["id"]  == payload.id:
            expenses.pop(idx)
            save_expenses(expenses)
            return transaction
        

def create_expenses(payload: ExpenseCreate):
    # open the notebook
    expenses = load_expenses()
    
    # build the new expense with server generated fields
    new_expense = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "merchant": payload.merchant,
        "description": payload.description,
        "category": payload.category,
        "amount": payload.amount,
        "created_at": datetime.utcnow().isoformat()
    }
    
    # append to list and save
    expenses.append(new_expense)
    save_expenses(expenses)
    
    # return the new expense
    return new_expense

def update_expenses(payload: ExpenseUpdate):
    # open the notebook
    expenses = load_expenses()

    # loop through storage to find the id
    for idx, transaction in enumerate(expenses):
        if transaction["id"] == payload.id:
            
            # only update fields that are not None
            if payload.title is not None:
                transaction["title"] = payload.title
            if payload.merchant is not None:
                transaction["merchant"] = payload.merchant
            if payload.description is not None:
                transaction["description"] = payload.description
            if payload.amount is not None:
                transaction["amount"] = payload.amount
                
            # save and return
            expenses[idx] = transaction
            save_expenses(expenses)
            return transaction

    raise HTTPException(status_code=404, detail="Not found")   