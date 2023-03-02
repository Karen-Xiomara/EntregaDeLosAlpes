from __future__ import annotations
from dataclasses import dataclass, field
from ordenonline.modulos.ordenes.dominio.eventos import OrdenCreada
import ordenonline.modulos.ordenes.dominio.objetos_valor as ov
from ordenonline.seedwork.dominio.entidades import  AgregacionRaiz
import uuid


@dataclass
class Orden(AgregacionRaiz):
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.PENDIENTE)
    def crear_orden(self, orden: Orden):
        self.estado = orden.estado
        self.agregar_evento(OrdenCreada(id=self.id,id_orden=self.id, estado=self.estado, fecha_creacion=self.fecha_creacion))