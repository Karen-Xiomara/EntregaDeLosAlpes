from pedido.config.db import db
from pedido.modulos.pedidos.dominio.repositorios import RepositorioPedido
from pedido.modulos.pedidos.dominio.entidades import Pedido
from .dto import Pedido as PedidoDTO
from uuid import UUID

class RepositorioPedidoSQLite(RepositorioPedido):

    def obtener_por_id(self, id: UUID) -> Pedido:
        pedido_dto = db.session.query(PedidoDTO).filter_by(id=str(id)).one()
        return pedido_dto
    
    def obtener_todos(self) -> list[Pedido]:
        # TODO
        raise NotImplementedError
    
    def agregar(self, entity: Pedido):
        db.session.add(entity)
    
    def actualizar(self, entity: Pedido):
        # TODO
        raise NotImplementedError
    
    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError