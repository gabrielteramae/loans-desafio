from fastapi import FastAPI
from app.schemas import CustomerRequest, CustomerLoansResponse
from app.loan_engine import determine_loans

app = FastAPI(
    title="Loans API",
    description="Determina quais modalidades de emprestimo um cliente tem acesso",
    version="1.0.0",
)


@app.post("/customer-loans", response_model=CustomerLoansResponse)
def customer_loans(customer: CustomerRequest):
    loans = determine_loans(customer.age, customer.income, customer.location)
    return CustomerLoansResponse(customer=customer.name, loans=loans)
