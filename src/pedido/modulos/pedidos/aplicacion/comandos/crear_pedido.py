from pedido.seedwork.aplicacion.comandos import Comando
from pedido.seedwork.aplicacion.comandos import ejecutar_commando as comando
from pedido.modulos.pedidos.aplicacion.dto import PedidoDTO
from pedido.modulos.pedidos.infraestructura.repositorios import RepositorioPedido
from pedido.modulos.pedidos.aplicacion.mapeadores import MapeadorPedido
from pedido.modulos.pedidos.dominio.entidades import Pedido

from dataclasses import dataclass
from .base import CrearPedidoBaseHandler

from pedido.seedwork.infraestructura.uow import UnidadTrabajoPuerto

@dataclass
class CrearPedido(Comando):
    id_client: str
    fecha_orden: str
    numero_orden: str

class CrearPedidoHandler(CrearPedidoBaseHandler):
    def handle(self, comando: CrearPedido):
        pedido_dto = PedidoDTO(
            id_client=comando.id_client, 
            fecha_orden=comando.fecha_orden, 
            numero_orden=comando.numero_orden)
        pedido: Pedido = self.fabrica_pedido.crear_objeto(pedido_dto, MapeadorPedido())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPedido.__class__)
        #repositorio.agregar(pedido)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, pedido)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPedido)
def ejecutar_comando_crear_pedido(comando: CrearPedido):
    handler = CrearPedidoHandler()
    handler.handle(comando)