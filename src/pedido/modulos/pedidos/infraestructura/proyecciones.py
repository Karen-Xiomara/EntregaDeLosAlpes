from pedido.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from pedido.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from pedido.modulos.pedidos.infraestructura.fabricas import FabricaRepositorio
from pedido.modulos.pedidos.infraestructura.repositorios import RepositorioPedido
from pedido.modulos.pedidos.dominio.entidades import Pedido

from pedido.seedwork.infraestructura.utils import millis_a_datetime
import datetime
import logging
import traceback
from abc import ABC, abstractmethod

from pedido.seedwork.infraestructura.uow import UnidadTrabajoPuerto

class ProyeccionPedido(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

# class ProyeccionPedidosTotales(ProyeccionPedido):
#     ADD = 1
#     DELETE = 2
#     UPDATE = 3

#     def __init__(self, fecha_creacion, operacion):
#         self.fecha_creacion = millis_a_datetime(fecha_creacion)
#         self.operacion = operacion

#     def ejecutar(self, db=None):
#         if not db:
#             logging.error('ERROR: DB del app no puede ser nula')
#             return
#         # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
#         record = db.session.query(Pedido).filter_by(fecha_creacion=self.fecha_creacion.date()).one_or_none()

#         if record and self.operacion == self.ADD:
#             record.total += 1
#         elif record and self.operacion == self.DELETE:
#             record.total -= 1 
#             record.total = max(record.total, 0)
#         else:
#             db.session.add(Pedido(fecha_creacion=self.fecha_creacion.date(), total=1))
        
#         db.session.commit()

class ProyeccionPedidosLista(ProyeccionPedido):
    def __init__(self, id_client, numero_orden, fecha_orden):
        self.id_client = id_client
        self.numero_orden = numero_orden
        self.fecha_orden = fecha_orden
    
    def ejecutar(self, app=None):
        if not app:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioPedido)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        pedido = Pedido(
                id_client=str(self.id_client), 
                numero_orden=str(self.numero_orden), 
                fecha_orden=self.fecha_orden)

        with app.test_request_context():
            UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, pedido)
            UnidadTrabajoPuerto.savepoint()
            UnidadTrabajoPuerto.commit()
        # TODO ¿Y si la pedido ya existe y debemos actualizarla? Complete el método para hacer merge

        # TODO ¿Tal vez podríamos reutilizar la Unidad de Trabajo?
        #db.session.commit()

class ProyeccionPedidoHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionPedido, app=None):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from pedido.config.db import db
        proyeccion.ejecutar(app=app)
        

@proyeccion.register(ProyeccionPedidosLista)
# @proyeccion.register(ProyeccionPedidosTotales)
def ejecutar_proyeccion_pedido(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionPedidoHandler()
            handler.handle(proyeccion, app)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
    