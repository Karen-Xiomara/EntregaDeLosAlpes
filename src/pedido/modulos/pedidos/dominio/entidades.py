from __future__ import annotations
from dataclasses import dataclass, field
from pedido.seedwork.dominio.entidades import AgregacionRaiz
from pedido.modulos.pedidos.dominio.eventos import PedidoCreado
from datetime import datetime
import uuid

@dataclass
class Pedido(AgregacionRaiz):
    id_client: uuid.UUID = field(hash=True, default=None)
    fecha_orden: datetime = field(default=None)
    numero_orden: str = field(default=None)

    def crear_pedido(self, pedido: Pedido):
        #self.estado = pedido.estado
        self.agregar_evento(PedidoCreado(id_cliente=self.id_client, numero_orden=self.numero_orden, fecha_orden=self.fecha_orden))