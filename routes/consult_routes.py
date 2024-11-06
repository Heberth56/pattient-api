from fastapi import APIRouter
from controllers.medicion_controllers import add_consult, list_consults, remove_consult, busqueda_mensual_anual
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


@router.get("/importe/{anio}")
async def list_importe_router(anio: int):
    return busqueda_mensual_anual(anio)


@router.delete("/remove/{consult_id}")
async def remove_consult_router(consult_id: str):
    return remove_consult(consult_id)
