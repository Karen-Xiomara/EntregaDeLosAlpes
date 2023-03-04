from pulsar.schema import *
from dataclasses import dataclass, field
from pedido.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPedidoPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearPedido(ComandoIntegracion):
    data = ComandoCrearPedidoPayload() 