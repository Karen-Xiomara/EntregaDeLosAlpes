import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)


class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class PedidoCreadoPayload(Record):
    id_orden = String()
    id_client = String()
    estado = String()
    fecha_creacion = Long()
    numero_orden = String()
    fecha_orden = String()

class EventoPedidoCreado(EventoIntegracion):
    data = PedidoCreadoPayload()




HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('eventos-pedido', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-eventos-pedidos', schema=AvroSchema(EventoPedidoCreado))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()