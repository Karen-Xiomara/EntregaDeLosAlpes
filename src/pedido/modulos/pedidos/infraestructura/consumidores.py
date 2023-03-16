import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from ordenonline.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada
#from ordenonline.modulos.ordenes.infraestructura.schema.v1.comandos import ComandoCrearOrden
from pedido.seedwork.infraestructura import utils

from pedido.modulos.pedidos.aplicacion.comandos.crear_pedido import CrearPedido
from pedido.seedwork.aplicacion.comandos import ejecutar_commando
from pedido.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from pedido.modulos.pedidos.infraestructura.proyecciones import ProyeccionPedidosLista
def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='orden-sub-eventos', schema=AvroSchema(EventoOrdenCreada))

        while True:
            mensaje = consumidor.receive()  
            datos = mensaje.value().data
            print(f'Evento recibido 1 : {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            #ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionPedidosLista(datos.id_orden, datos.fecha_creacion, datos.id_orden), app=app)

            # with app.app_context():           
            #     comando = CrearPedido(id_client=mensaje.value().data.id_orden, 
            #         fecha_orden= mensaje.value().data.fecha_creacion, 
            #         numero_orden=mensaje.value().data.id_orden)
            #     ejecutar_commando(comando)

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
        #consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='orden-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

        # while True:
        #     mensaje = consumidor.receive()
        #     print(f'Comando recibido: {mensaje.value().data}')

        #     consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
