
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
from datetime import datetime
import logging
import traceback

from ordenonline.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada, EventoSagaEjecutar
from ordenonline.modulos.ordenes.infraestructura.schema.v1.comandos import ComandoCrearOrden
from ordenonline.seedwork.infraestructura import utils
from ordenonline.modulos.sagas.aplicacion.coordinadores.saga_orden import CoordinadorOrdenes
from ordenonline.seedwork.dominio.eventos import EventoDominio
from ordenonline.modulos.ordenes.dominio.eventos import OrdenCreada
from ordenonline.seedwork.infraestructura.schema.v1.mensajes import Mensaje




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


#        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "ejecutar-saga", "public/default/comandos-orden")

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='ordenonline-sub-comandos-orden', schema=AvroSchema(ComandoCrearOrden))

        while True:            
            mensaje = consumidor.receive()
            valor = mensaje.value()
            print(f'Comando recibido: {mensaje.value().data}')
            
            fecha_creacion = utils.millis_a_datetime(valor.data.fecha_creacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            fecha_actualizacion = utils.millis_a_datetime(valor.data.fecha_actualizacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            id = str(uuid.uuid4())
            
            try:
                with app.test_request_context():
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

def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorOrdenes()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")

def suscribirse_a_ejecutar_saga(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('ejecutar-saga', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='ordenonline-sub-comandos-orden', schema=AvroSchema(ComandoCrearOrden))
        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido SA: {mensaje.value().data}')

            order = OrdenCreada(id="asdfasdfasdfasdf", id_orden=10,estado="1")
            oir_mensaje(order)
            print(f'He oido el mensaje: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)


        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de ejecutar-saga!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def mensaje_a_evento(mensaje):
    print(mensaje)
    #id = uuid.UUID(mensaje.id)
    fecha_evento = datetime.fromtimestamp(mensaje.time / 1000.0)
    evento = EventoDominio(id=id, fecha_evento=fecha_evento)
    return evento