from pydantic import BaseModel, Field
from datetime import datetime


class Consult(BaseModel):
    fecha: datetime = Field(example="2023-04-02T00:00:00")
    patient_id: str = Field(example="123456789")
    medicion_type: str = Field(example="1")
    costo: int = Field(example="250")
