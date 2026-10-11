from pydantic import BaseModel, Field

class Expense(BaseModel):
    model_config = {"str_strip_whitespace": True}

    name: str = Field(min_length=1, max_length=35)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=20)
