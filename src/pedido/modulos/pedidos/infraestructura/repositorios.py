from pedido.config.db import db
from pedido.modulos.pedidos.dominio.repositorios import RepositorioPedido
from pedido.modulos.pedidos.dominio.entidades import Pedido
from pedido.modulos.pedidos.dominio.fabricas import FabricaPedido
from .dto import Pedido as PedidoDTO
from .mapeadores import MapeadorPedido
from uuid import UUID

class RepositorioPedidoSQLite(RepositorioPedido):

    def __init__(self):
        self._fabrica_pedido: FabricaPedido = FabricaPedido()

    @property
    def fabrica_pedido(self):
        return self._fabrica_pedido

    def obtener_por_id(self, id: UUID) -> Pedido:
        pedido_dto = db.session.query(PedidoDTO).filter_by(id=str(id)).one()
        return pedido_dto
    
    def obtener_todos(self) -> list[Pedido]:
        # TODO
        raise NotImplementedError
    
    def agregar(self, entity: Pedido):
        pedido_dto = self.fabrica_pedido.crear_objeto(entity, MapeadorPedido())
        db.session.add(pedido_dto)
        db.session.commit()
    
    def actualizar(self, entity: Pedido):
        # TODO
        raise NotImplementedError
    
    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError