from pedido.seedwork.aplicacion.comandos import Comando
from pedido.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pedido.modulos.pedidos.aplicacion.dto import PedidoDTO
from pedido.modulos.pedidos.infraestructura.repositorios import RepositorioPedido
from dataclasses import dataclass
from .base import CrearPedidoBaseHandler

@dataclass
class CrearPedido(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str

class CrearPedidoHandler(CrearPedidoBaseHandler):
    def handle(self, comando: CrearPedido):
        pedido_dto = PedidoDTO(id=comando.id, 
        fecha_actualizacion=comando.fecha_actualizacion, 
        fecha_creacion=comando.fecha_creacion)
        
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPedido.__class__)
        repositorio.agregar()

@comando.register(CrearPedido)
def ejecutar_comando_crear_pedido(comando: CrearPedido):
    handler = CrearPedidoHandler()
    handler.handle(comando)