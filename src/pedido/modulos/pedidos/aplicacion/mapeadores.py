from pedido.seedwork.aplicacion.dto import Mapeador as AppMap
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