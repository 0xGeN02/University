from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/salas",
    tags=["Salas"],
    responses={404: { 'description': "Not Found"}}
)

#Rutas CRUD
@router.get("/")
def read_salas():
    return{ "message": "Listado de salas"}

@router.post("/")
def create_sala(sala: dict):
    return {"message": "Sala creada", "sala": sala}