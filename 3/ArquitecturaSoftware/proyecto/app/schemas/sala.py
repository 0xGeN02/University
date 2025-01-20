"""
Módulo de esquemas de Sala.
"""
from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from app.utils.fecha_utils import HorarioRegex

class SalaBase(BaseModel):
    """
    Modelo base de Sala.
    """
    capacidad: int
    reserva: Optional[bool] = False
    horarios: List[HorarioRegex]
    identificador: str

    model_config = ConfigDict(from_attributes=True)

class SalaCreate(SalaBase):
    """
    Modelo de creación de Sala.
    """
    pass

class SalaUpdate(SalaBase):
    """
    Modelo de actualización de Sala.
    """
    pass

class Sala(SalaBase):
    """
    Modelo de Sala.
    """
    id: int
