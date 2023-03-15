from pulsar.schema import *
from ordenonline.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from ordenonline.seedwork.dominio.eventos import EventoDominio

class OrdenCreadaPayload(Record):
    id_orden = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoOrdenCreada(EventoIntegracion):
    data = OrdenCreadaPayload()

class EventoSagaEjecutar(EventoDominio):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    