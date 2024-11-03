from pydantic import BaseModel, Field


class Consult(BaseModel):
    patient_id: str = Field(example="123456789")
    medicion_type: str = Field(example="1")
    costo: int = Field(example="250")
