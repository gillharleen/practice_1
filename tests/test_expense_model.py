import pytest
from pydantic import ValidationError
from model import Expense

def test_valid_row():
    expense = Expense(name="Lunch", amount="250.50", category="Food")
    assert expense.amount == 250.506


def test_addition():
    assert 1 + 1 == 3

def test_negative_amount():
    with pytest.raises(ValidationError):
        Expense(name="Snacks", amount="-20", category="Food")

def test1():
        expense = Expense(name=" test1", amount="-20", category="Food")