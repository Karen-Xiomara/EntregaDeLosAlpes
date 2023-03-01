from __future__ import annotations
from dataclasses import dataclass
from ordenonline.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid


@dataclass
class OrdenCreada(EventoDominio):
    id_orden: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None