from pydantic import BaseModel, Field


class CustomerRequest(BaseModel):
    age: int = Field(gt=0)
    cpf: str
    name: str
    income: float = Field(ge=0)
    location: str


class LoanOffer(BaseModel):
    type: str
    interest_rate: float


class CustomerLoansResponse(BaseModel):
    customer: str
    loans: list[LoanOffer]
