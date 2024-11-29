from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {"description": "Not found"}}
)

# Rutas para CRUD de usuarios
@router.get("/")
def read_users():
    return {"message": "Listado de usuarios"}

@router.post("/")
def create_user(user: dict):
    return {"message": "Usuario creado", "user": user}
