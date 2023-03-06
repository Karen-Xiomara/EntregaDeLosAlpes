from pedido.seedwork.aplicacion.dto import Mapeador as AppMap
from pedido.seedwork.dominio.repositorios import Mapeador as RepMap
from pedido.modulos.pedidos.dominio.entidades import Pedido
from .dto import PedidoDTO
from datetime import datetime

class MapeadorPedidoDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PedidoDTO:
        pedido_dto = PedidoDTO(
            id_client=externo.get('id_client'),
            fecha_orden=externo.get('fecha_orden'),
            numero_orden=externo.get('numero_orden')
        )
        return pedido_dto

    def dto_a_externo(self, dto: PedidoDTO) -> dict:
        return dto.__dict__

class MapeadorPedido(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pedido.__class__

    def entidad_a_dto(self, entidad: Pedido) -> PedidoDTO:
        return PedidoDTO(
            id_client = str(entidad.id_client), 
            fecha_orden = datetime.strftime(entidad.fecha_orden, self._FORMATO_FECHA), 
            numero_orden = entidad.numero_orden)

    def dto_a_entidad(self, dto: PedidoDTO) -> Pedido:
        pedido = Pedido(id_client=dto.id_client, fecha_orden=dto.fecha_orden, numero_orden=dto.numero_orden)
        return pedido