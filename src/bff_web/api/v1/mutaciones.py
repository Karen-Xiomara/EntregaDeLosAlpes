import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    async def crear_orden(self, id: str, fecha_creacion:str, fecha_actualizacion:str, info: Info) -> OrdenRespuesta:
        print(f"ID : {id}")
        payload = dict(
            id = id,
            fecha_creacion = utils.time_millis(),
            fecha_actualizacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoOrden",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-orden", "public/default/comandos-orden")
        
        return OrdenRespuesta(mensaje="Procesando Mensaje", codigo=203)