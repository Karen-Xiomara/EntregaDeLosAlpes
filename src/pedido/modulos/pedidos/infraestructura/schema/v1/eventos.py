from pulsar.schema import *
from pedido.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PedidoCreadoPayload(Record):
    id_cliente = String()
    numero_orden = String()
    fecha_orden = String()

class EventoPedidoCreado(EventoIntegracion):
    data = PedidoCreadoPayload() 