from pedido.seedwork.aplicacion.comandos import Comando
from pedido.seedwork.aplicacion.comandos import ejecutar_commando as comando
from dataclasses import dataclass

@dataclass
class CrearPedido(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str

@comando.register(CrearPedido)
def ejecutar_comando_crear_pedido(comando: CrearPedido):
    handler = CrearPedidoHandler()
    handler.handle(comando)