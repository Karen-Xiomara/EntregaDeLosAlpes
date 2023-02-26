from dataclasses import dataclass, field
from pedido.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PedidoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)