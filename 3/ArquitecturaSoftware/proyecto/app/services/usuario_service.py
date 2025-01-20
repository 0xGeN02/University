"""
Este módulo contiene la lógica de negocio para la gestión de usuarios.
"""
import logging
import re
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from app.db.models import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.utils.crypto_utils import encrypt_message, decrypt_message

# Optional: Set up logging for better error tracking
logger = logging.getLogger(__name__)

async def get_usuario_by_id(usuario_id: int, db: AsyncSession, desencriptar: bool = False):
    """
    Obtiene un usuario por su ID en la base de datos.
    """
    result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = result.scalar_one_or_none()

    if usuario and desencriptar:
        try:
            logger.debug("Original DNI before any decryption: %s", usuario.dni)

            if hasattr(usuario, 'dni') and usuario.dni:
                # First decryption
                first_decryption = decrypt_message(usuario.dni)
                logger.debug("DNI after first decryption: %s", first_decryption)

                # Check if result is still encrypted
                if ':' in first_decryption:
                    # Second decryption
                    final_dni = decrypt_message(first_decryption)
                    logger.debug("DNI after second decryption: %s", final_dni)
                    usuario.dni = final_dni
                else:
                    usuario.dni = first_decryption
  
                # Validate final DNI format
                if not re.match(r'^\d{8}[A-Z]$', usuario.dni):
                    logger.warning("Final DNI does not match expected format: %s", usuario.dni)

            if hasattr(usuario, 'password') and usuario.password:
                if ':' in str(usuario.password):
                    usuario.password = decrypt_message(usuario.password)
                    logger.debug("Password decrypted: %s", usuario.password)

        except ValueError as e:
            logger.error("Decryption error: %s", str(e))
            raise HTTPException(
                status_code=500,
                detail=f"Error decrypting data for user {usuario_id}"
            ) from e
            
    return usuario

async def get_usuario_by_dni(dni: str, db: AsyncSession):
    """
    Obtiene un usuario por su DNI en la base de datos.
    """
    encrypted_dni = encrypt_message(dni)
    result = await db.execute(select(Usuario).where(Usuario.dni == encrypted_dni))
    return result.scalar_one_or_none()

async def get_usuario_by_correo(correo: str, db: AsyncSession):
    """
    Obtiene un usuario por su correo en la base de datos.
    """
    result = await db.execute(select(Usuario).where(Usuario.correo == correo))
    return result.scalar_one_or_none()

async def get_usuarios_by_nombre(nombre: str, db: AsyncSession):
    """
    Obtiene todos los usuarios por su nombre en la base de datos.
    """
    result = await db.execute(select(Usuario).where(Usuario.nombre == nombre))
    return result.scalars().all()

async def get_all_usuarios(db: AsyncSession):
    """
    Obtiene todos los usuarios en la base de datos.
    """
    result = await db.execute(select(Usuario))
    return result.scalars().all()

async def create_usuario(usuario: UsuarioCreate, db: AsyncSession):
    """
    Crea un nuevo usuario en la base de datos.
    """
    try:
        async with db.begin():
            existing_usuario = await get_usuario_by_dni(usuario.dni, db)
            if existing_usuario:
                raise ValueError("El usuario con este DNI ya existe.")

            encrypted_dni = encrypt_message(usuario.dni)
            encrypted_password = encrypt_message(usuario.password)
            logger.info("Encrypted DNI: %s", encrypted_dni)
            logger.info("Encrypted password: %s", encrypted_password)

            nuevo_usuario = Usuario(
                nombre=usuario.nombre,
                correo=usuario.correo,
                telefono=usuario.telefono,
                dni=encrypted_dni,
                password=encrypted_password
            )

            # Test decryption before saving
            test_dni = decrypt_message(encrypted_dni)
            logger.debug("Test DNI decryption: %s", test_dni)
            if test_dni != usuario.dni:
                raise ValueError("Encryption/decryption verification failed")

            db.add(nuevo_usuario)
            await db.flush()  # Ensure the user is added before committing
            await db.refresh(nuevo_usuario)
            return nuevo_usuario
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

async def delete_usuario_by_id(usuario_id: int, db: AsyncSession):
    """
    Elimina un usuario por su ID en la base de datos.
    """
    try:
        async with db.begin():
            result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
            usuario = result.scalar_one_or_none()
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            await db.delete(usuario)
            await db.commit()
            return {"detail": "Usuario eliminado correctamente"}
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"detail": "Usuario eliminado correctamente"}

async def update_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: AsyncSession):
    """
    Actualiza el correo o el teléfono de un usuario en la base de datos.
    """
    try:
        async with db.begin():
            result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
            usuario = result.scalar_one_or_none()
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            if usuario_update.correo:
                usuario.correo = usuario_update.correo
            if usuario_update.telefono:
                usuario.telefono = usuario_update.telefono

            await db.flush()
            await db.refresh(usuario)
            return usuario
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="El correo o el teléfono ya están en uso.") from e
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
    return (usuario_id, usuario_update)

async def patch_usuario(usuario_id: int, usuario_update: dict, db: AsyncSession):
    """
    Actualiza parcialmente un usuario en la base de datos.
    """
    try:
        async with db.begin():
            result = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
            usuario = result.scalar_one_or_none()
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            for key, value in usuario_update.items():
                setattr(usuario, key, value)

            await db.flush()
            await db.refresh(usuario)
            return usuario
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="El correo o el teléfono ya están en uso.") from e
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(e)}") from e
