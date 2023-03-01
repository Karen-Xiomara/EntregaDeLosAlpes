from dataclasses import dataclass
from pedido.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PedidoDTO(DTO):
    fecha_creacion: str 
    fecha_actualizacion: str 
    id: str 