from ordenonline.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.vuelos.aplicacion.dto import ItinerarioDTO, ReservaDTO
from ordenonline.modulos.ordenes.aplicacion.dto import ItinerarioDTO, OrdenDTO
from .base import CrearReservaBaseHandler
from .base import CrearOrdenBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas

@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    itinerarios: list[ItinerarioDTO]


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        reserva_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        reserva.crear_reserva(reserva)
        print('Esta usando orden')

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearOrden)
def ejecutar_comando_crear_reserva(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    