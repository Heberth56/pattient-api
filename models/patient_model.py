from pydantic import BaseModel, Field


class Patient(BaseModel):    
    name: str = Field(example="Jhon Bon")
    paterno: str = Field(example="Bon")
    materno: str = Field(example="Doe")
    age: int = Field(example=25)
    phone: str = Field(example="12345678")
