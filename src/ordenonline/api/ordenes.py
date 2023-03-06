import ordenonline.seedwork.presentacion.api as api
import json
from ordenonline.modulos.ordenes.aplicacion.dto import OrdenDTO
from ordenonline.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response
from ordenonline.modulos.ordenes.aplicacion.mapeadores import MapeadorOrdenDTOJson
from ordenonline.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from ordenonline.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('ordenes', '/ordenes')

@bp.route('/orden-comando', methods=('POST',))
def ordenar_asincrona():
    try:
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)

        comando = CrearOrden(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')