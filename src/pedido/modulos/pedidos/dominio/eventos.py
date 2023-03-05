from __future__ import annotations
from dataclasses import dataclass
from pedido.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class PedidoCreado(EventoDominio):
    id_cliente: str = None
    numero_orden: str = None
    fecha_orden: datetime = None