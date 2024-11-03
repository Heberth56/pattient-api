from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import patients_routes, consult_routes

app = FastAPI(
    title="PACIENTES",
    description="ENDPOINT PARA LAS OPEARCIONES PARA LOS PACIENTES",
    version="0.1.0",
    responses={
        404: {"description": "No encontrado"},
        500: {"description": "Error interno del servidor"},
        200: {"description": "Proceso exitoso"}
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patients_routes.router)
app.include_router(consult_routes.router)
