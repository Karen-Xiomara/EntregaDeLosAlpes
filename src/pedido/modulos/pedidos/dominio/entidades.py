from dataclasses import dataclass, field
from pedido.seedwork.dominio.entidades import AgregacionRaiz
from datetime import datetime
import uuid

@dataclass
class Pedido(AgregacionRaiz):
    id_client: uuid.UUID = field(hash=True, default=None)
    fecha_orden: datetime = field(default=None)
    numero_orden: str = field(default=None)