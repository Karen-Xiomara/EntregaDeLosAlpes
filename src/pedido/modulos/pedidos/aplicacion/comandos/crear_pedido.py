from pedido.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass

@dataclass
class CrearPedido(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str

