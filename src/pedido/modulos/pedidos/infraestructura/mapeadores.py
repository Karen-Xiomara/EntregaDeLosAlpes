from pedido.seedwork.dominio.repositorios import Mapeador
from pedido.modulos.pedidos.dominio.entidades import Pedido
from .dto import Pedido as PedidoDTO

class MapeadorPedido(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pedido.__class__

    def entidad_a_dto(self, entidad: Pedido) -> PedidoDTO:
        pedido_dto = PedidoDTO()
        pedido_dto.id = entidad.id
        pedido_dto.fecha_creacion = entidad.fecha_creacion
        pedido_dto.fecha_actualizacion = entidad.fecha_actualizacion
        pedido_dto.id_client = entidad.id_client
        pedido_dto.fecha_orden = entidad.fecha_orden
        pedido_dto.numero_orden = entidad.numero_orden

        return pedido_dto

    def dto_a_entidad(self, dto: PedidoDTO) -> Pedido:
        pedido = Pedido(id_client=dto.id_client, 
        fecha_orden=dto.fecha_orden, 
        numero_orden=dto.numero_orden)

        return pedido