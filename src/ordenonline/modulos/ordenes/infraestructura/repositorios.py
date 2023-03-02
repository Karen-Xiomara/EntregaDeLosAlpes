""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from ordenonline.config.db import db
from ordenonline.modulos.ordenes.aplicacion.dto import OrdenDTO
from ordenonline.modulos.ordenes.dominio.entidades import Orden
from ordenonline.modulos.ordenes.dominio.fabricas import FabricaOrdenes
from ordenonline.modulos.ordenes.dominio.repositorios import RepositorioOrdenes
from .mapeadores import MapeadorOrden
from uuid import UUID



class RepositorioOrdenesSQLite(RepositorioOrdenes):

    def __init__(self):
        self._fabrica_ordenes: FabricaOrdenes = FabricaOrdenes()

    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes

    def obtener_por_id(self, id: UUID) -> Orden:
        orden_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        return self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())

    def obtener_todos(self) -> list[Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        orden_dto = self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())
        db.session.add(orden_dto)


    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError