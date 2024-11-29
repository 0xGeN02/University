from fastapi import FastAPI
from app.api import routes_salas, routes_users

app = FastAPI()

# Registrar rutas
app.include_router(routes_salas.router)
app.include_router(routes_users.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Gestión de Salas"}
