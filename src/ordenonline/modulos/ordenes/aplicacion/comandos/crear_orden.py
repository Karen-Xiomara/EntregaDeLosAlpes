from ordenonline.seedwork.aplicacion.comandos import Comando
from ordenonline.modulos.ordenes.aplicacion.dto import OrdenDTO
from .base import CrearOrdenBaseHandler
from dataclasses import dataclass, field
from ordenonline.seedwork.aplicacion.comandos import ejecutar_commando as comando
from ordenonline.api import create_app

from ordenonline.modulos.ordenes.dominio.entidades import Orden
from ordenonline.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from ordenonline.modulos.ordenes.aplicacion.mapeadores import MapeadorOrden
from ordenonline.modulos.ordenes.infraestructura.repositorios import RepositorioOrdenes
#from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas

@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
   



class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id)

        orden: Orden  = self._fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())
        orden.crear_orden(orden)

        
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        repositorio.agregar(orden)
        """
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()"""

@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    