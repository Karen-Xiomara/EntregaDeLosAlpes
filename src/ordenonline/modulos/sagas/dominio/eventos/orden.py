from __future__ import annotations
from dataclasses import dataclass
from ordenonline.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

class EventoOrden(EventoDominio):
    ...

@dataclass
class OrdenCreada(EventoOrden):
    id_orden: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class OrdenCancelada(EventoOrden):
    id_orden: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class OrdenFallida(EventoOrden):
    id_orden: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None