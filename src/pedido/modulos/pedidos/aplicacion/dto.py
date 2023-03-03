from dataclasses import dataclass
from pedido.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PedidoDTO(DTO):
    id_client: str 
    fecha_orden: str
    numero_orden: str