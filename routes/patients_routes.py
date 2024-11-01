from fastapi import APIRouter, Depends
from controllers.patient_controllers import add_patient, edit_patient, list_patient, remove_patient, get_patient
from models.patient_model import Patient

router = APIRouter(
    prefix="/clientes",
    tags=["CRUD CLIENTES DATA BASE"]
)


@router.post("/add")
async def add_patient_router(model: Patient):
    return add_patient(model)


@router.put("/edit/{patient_id}")
async def edit_patient_router(model: Patient, patient_id: str):
    return edit_patient(model, patient_id)


@router.get("/list")
async def list_patient_router():
    return list_patient()


@router.get("/get-patient/{patient_id}")
async def get_patient_router(patient_id: str):
    return get_patient(patient_id)


@router.delete("/remove/{patient_id}")
async def list_patient_router(patient_id: str):
    return remove_patient(patient_id)
