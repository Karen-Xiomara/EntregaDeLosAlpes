from pulsar.schema import *
from dataclasses import dataclass, field
from ordenonline.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from ordenonline.seedwork.infraestructura.utils import time_millis
import uuid

class ComandoCrearOrdenPayload(ComandoIntegracion):
    id = String()
    fecha_creacion = Long()
    fecha_actualizacion = Long()

class ComandoCrearOrden(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearOrdenPayload()    