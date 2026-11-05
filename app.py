print("Hello")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Finance Routes
@app.get("/finance/summary")
def finance_summary():
    return {"total_budget": 500000, "spent": 320000, "remaining": 180000}

@app.get("/finance/transactions")
def transactions():
    return {"transactions": [
        {"id": 1, "type": "expense", "amount": 5000, "desc": "Office Rent"},
        {"id": 2, "type": "income", "amount": 20000, "desc": "Client Payment"},
    ]}

# Recruitment Routes
@app.get("/recruitment/jobs")
def jobs():
    return {"jobs": [
        {"id": 1, "title": "Software Engineer", "status": "Open"},
        {"id": 2, "title": "HR Manager", "status": "Closed"},
    ]}

@app.get("/recruitment/candidates")
def candidates():
    return {"candidates": [
        {"id": 1, "name": "Ali Khan", "role": "Software Engineer", "status": "Interview"},
        {"id": 2, "name": "Sara Ahmed", "role": "HR Manager", "status": "Selected"},
    ]}

# Workforce Routes
@app.get("/workforce/employees")
def employees():
    return {"employees": [
        {"id": 1, "name": "John Doe", "dept": "Finance", "status": "Active"},
        {"id": 2, "name": "Jane Smith", "dept": "HR", "status": "Active"},
    ]}

@app.get("/workforce/attendance")
def attendance():
    return {"attendance": [
        {"emp_id": 1, "name": "John Doe", "present": 22, "absent": 2},
        {"emp_id": 2, "name": "Jane Smith", "present": 24, "absent": 0},
    ]}
