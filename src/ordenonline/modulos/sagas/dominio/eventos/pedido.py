from __future__ import annotations
from dataclasses import dataclass
from ordenonline.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

class EventoPedido(EventoDominio):
    ...

@dataclass
class PedidoCreado(EventoDominio):
    id_cliente: str = None
    numero_orden: str = None
    fecha_orden: datetime = None


@dataclass
class PedidoCancelado(EventoDominio):
    id_cliente: str = None
    numero_orden: str = None
    fecha_orden: datetime = None

@dataclass
class PedidoRevertido(EventoDominio):
    id_cliente: str = None
    numero_orden: str = None
    fecha_orden: datetime = None