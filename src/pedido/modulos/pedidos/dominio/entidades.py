from dataclasses import dataclass, field
from pedido.seedwork.dominio.entidades import Entidad
import uuid

@dataclass
class Pedido(Entidad):
    id: uuid.UUID = field(hash=True, default=None)