from pulsar.schema import *
from pedido.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PedidoCreadoPayload(Record):
    id_pedido = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoPedidoCreado(EventoIntegracion):
    data = PedidoCreadoPayload() 