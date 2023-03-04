from pedido.seedwork.aplicacion.queries import QueryHandler
from pedido.modulos.pedidos.infraestructura.fabricas import FabricaRepositorio
from pedido.modulos.pedidos.dominio.fabricas import FabricaPedido

class PedidoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_pedido: FabricaPedido = FabricaPedido()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_pedido(self):
        return self._fabrica_pedido 