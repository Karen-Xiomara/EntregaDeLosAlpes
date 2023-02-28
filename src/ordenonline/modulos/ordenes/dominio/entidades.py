"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import ordenonline.modulos.ordenes.dominio.objetos_valor as ov
from ordenonline.modulos.vuelos.dominio.eventos import OrdenCreada
from ordenonline.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Orden(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.PENDIENTE)
    
   

    def crear_orden(self, orden: Orden):
        self.id_cliente = orden.id_cliente
        self.estado = orden.estado

        self.agregar_evento(OrdenCreada(id_orden=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))
"""
    def aprobar_reserva(self):
        self.estado = ov.EstadoReserva.APROBADA

        self.agregar_evento(ReservaAprobada(self.id, self.fecha_actualizacion))

    def cancelar_reserva(self):
        self.estado = ov.EstadoReserva.CANCELADA

        self.agregar_evento(ReservaCancelada(self.id, self.fecha_actualizacion))
    
    def pagar_reserva(self):
        self.estado = ov.EstadoReserva.PAGADA

        self.agregar_evento(ReservaPagada(self.id, self.fecha_actualizacion))
"""