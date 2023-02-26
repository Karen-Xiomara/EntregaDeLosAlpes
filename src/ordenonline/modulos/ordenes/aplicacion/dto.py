from dataclasses import dataclass, field
from ordenonline.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str