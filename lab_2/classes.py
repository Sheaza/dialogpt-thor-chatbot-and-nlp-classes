from pydantic import BaseModel
from datetime import datetime


class Employee(BaseModel):
    name: str
    surname: str
    salary: int


class ReceivedInvoice(BaseModel):
    date: datetime
    amount: int


class IssuedInvoice(BaseModel):
    date: datetime
    amount: int

