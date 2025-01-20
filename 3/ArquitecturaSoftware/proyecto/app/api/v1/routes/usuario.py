"""
    Aqui se definen las rutas de la API para el recurso Usuario
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.services.usuario_service import (create_usuario as service_create_usuario, get_usuario_by_id,
                                        delete_usuario_by_id, update_usuario as service_update_usuario,
                                        get_usuario_by_correo, patch_usuario as service_patch_usuario,
                                        get_usuarios_by_nombre, get_all_usuarios)
from app.db.session import get_db
from app.utils.crypto_utils import decrypt_message

router = APIRouter()

@router.post("/usuario", response_model=Usuario)
async def route_create_usuario(usuario: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    """
    Crea un nuevo usuario
    """
    try:
        nuevo_usuario = await service_create_usuario(usuario, db)
        return nuevo_usuario
    except IntegrityError as exec:
        raise HTTPException(status_code=400, detail="El usuario ya existe.") from exec

@router.get("/usuario/{usuario_id}", response_model=Usuario)
async def route_read_usuario(usuario_id: int, db: AsyncSession = Depends(get_db), desencriptar: bool = False):
    """
    Obtiene un usuario por su id
    """
    usuario = await get_usuario_by_id(usuario_id, db, desencriptar=desencriptar)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/usuarios", response_model=list[Usuario])
async def route_get_all_usuarios(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los usuarios
    """
    usuarios = await get_all_usuarios(db)
    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios")
    return usuarios

@router.get("/usuarios/nombre/{nombre}", response_model=list[Usuario])
async def route_get_usuarios_by_correo(nombre: str, db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los usuarios por su correo electrónico
    """
    usuarios = await get_usuarios_by_nombre(nombre, db)
    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios con ese correo electrónico")
    return usuarios

@router.delete("/usuario/{usuario_id}")
async def route_delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    """
    Elimina un usuario por su id
    """
    return await delete_usuario_by_id(usuario_id, db)

@router.put("/usuario/{usuario_id}", response_model=Usuario)
async def route_update_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    """
    Actualiza el correo o el teléfono de un usuario
    """
    return await service_update_usuario(usuario_id, usuario_update, db)

@router.head("/usuario/correo/{correo}")
async def route_head_usuario_by_correo(correo: str, db: AsyncSession = Depends(get_db)):
    """
    Verifica si un usuario existe por su correo electrónico
    """
    usuario = await get_usuario_by_correo(correo, db)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None

@router.options("/usuario")
async def route_options_usuario():
    """
    Devuelve las opciones permitidas para el recurso usuario
    """
    return {
        "methods": ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "TRACE", "PATCH"],
    }

@router.trace("/usuario")
async def route_trace_usuario(request: Request):
    """
    Devuelve la solicitud recibida para el recurso usuario
    """
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "body": await request.body()
    }

@router.patch("/usuario/{usuario_id}", response_model=Usuario)
async def route_patch_usuario(usuario_id: int, usuario_update: dict, db: AsyncSession = Depends(get_db)):
    """
    Actualiza parcialmente un usuario
    """
    return await service_patch_usuario(usuario_id, usuario_update, db)
