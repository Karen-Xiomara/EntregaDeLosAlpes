from dataclasses import dataclass
from pedido.seedwork.dominio.entidades import Entidad

@dataclass
class Pedido(Entidad):
    id: uuid.UUID = field(hash=True, default=None)