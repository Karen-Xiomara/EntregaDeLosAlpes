from pedido.seedwork.aplicacion.dto import Mapeador as AppMap
from pedido.seedwork.dominio.repositorios import Mapeador as RepMap
from pedido.modulos.pedidos.dominio.entidades import Pedido
from .dto import PedidoDTO

class MapeadorPedidoDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PedidoDTO:
        pedido_dto = PedidoDTO(
            externo.get('id'),
            externo.get('fecha_creacion'),
            externo.get('fecha_actualizacion')
        )

        return pedido_dto

    def dto_a_externo(self, dto: PedidoDTO) -> dict:
        return dto.__dict__


class MapeadorPedido(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pedido.__class__

    def entidad_a_dto(self, entidad: Pedido) -> PedidoDTO:
        _id = str(entidad.id)
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)

        return PedidoDTO(fecha_creacion, fecha_actualizacion, _id)