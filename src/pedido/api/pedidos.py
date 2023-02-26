import pedido.seedwork.presentacion.api as api
import json
from pedido.seedwork.dominio.excepciones import ExcepcionDominio
from flask import Response
from pedido.modulos.pedidos.aplicacion.mapeadores import MapeadorPedidoDTOJson

bp = api.crear_blueprint('pedidos', '/pedidos')

@bp.route('/pedido-comando', methods=('POST',))
def reservar_asincrona():

    try:
        pedido_dict = request.json

        map_pedido = MapeadorPedidoDTOJson()
        pedido_dto = map_pedido.externo_a_dto(pedido_dict) 


        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')