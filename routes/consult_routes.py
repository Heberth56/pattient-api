from fastapi import APIRouter
from controllers.medicion_controllers import add_consult, list_consults
from models.medicion_model import Consult

router = APIRouter(
    prefix="/consult",
    tags=["CRUD CONSULT DATA BASE"]
)


@router.post("/add")
async def add_consult_router(model: Consult):
    return add_consult(model)


@router.get("/list")
async def list_consult_router():
    return list_consults()
