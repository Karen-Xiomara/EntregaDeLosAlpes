from __future__ import annotations
from dataclasses import dataclass, field
from ordenonline.modulos.ordenes.dominio.eventos import OrdenCreada
import ordenonline.modulos.ordenes.dominio.objetos_valor as ov
from ordenonline.seedwork.dominio.entidades import  AgregacionRaiz
import uuid


@dataclass
class Orden(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)    
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.PENDIENTE)
    def crear_orden(self, orden: Orden):
        self.id_cliente = orden.id_cliente
        self.estado = orden.estado
        self.agregar_evento(OrdenCreada(id=self.id,id_orden=self.id, id_cliente=self.id_cliente, estado=self.estado, fecha_creacion=self.fecha_creacion))