
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from ordenonline.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada
from ordenonline.modulos.ordenes.infraestructura.schema.v1.comandos import ComandoCrearOrden
from ordenonline.seedwork.infraestructura import utils


from ordenonline.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from ordenonline.seedwork.aplicacion.comandos import ejecutar_commando

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='ordenonline-sub-eventos', schema=AvroSchema(EventoOrdenCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='ordenonline-sub-comandos-orden', schema=AvroSchema(ComandoCrearOrden))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            
            fecha_creacion = utils.millis_a_datetime(valor.data.fecha_creacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            fecha_actualizacion = utils.millis_a_datetime(valor.data.fecha_actualizacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            id = str(uuid.uuid4())
            
            try:
                with app.app_context():
                    comando = CrearOrden(fecha_creacion, fecha_actualizacion, id)
                    ejecutar_commando(comando)
            except:
                logging.error('ERROR: Procesando eventos!')
                traceback.print_exc()

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

            