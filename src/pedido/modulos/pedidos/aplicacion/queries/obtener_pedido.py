from dataclasses import dataclass
from pedido.seedwork.aplicacion.queries import Query, QueryResultado
from pedido.seedwork.aplicacion.queries import ejecutar_query as query
from pedido.modulos.pedidos.infraestructura.repositorios import RepositorioPedido
from pedido.modulos.pedidos.aplicacion.mapeadores import MapeadorPedido
from .base import PedidoQueryBaseHandler

@dataclass
class ObtenerPedido(Query):
    id: str

class ObtenerPedidoHandler(PedidoQueryBaseHandler):
    def handle(self, query: ObtenerPedido) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPedido.__class__)
        pedido = self.fabrica_pedido.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPedido())
        return QueryResultado(resultado = pedido)

@query.register(ObtenerPedido)
def ejecutar_query_obtener_pedido(query: ObtenerPedido):
    handler = ObtenerPedidoHandler()
    return handler.handle(query)