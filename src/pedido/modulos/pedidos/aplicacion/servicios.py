from pedido.seedwork.aplicacion.servicios import Servicio
from pedido.modulos.pedidos.dominio.fabricas import FabricaPedido
from pedido.modulos.pedidos.infraestructura.fabricas import FabricaRepositorio
from pedido.modulos.pedidos.infraestructura.repositorios import RepositorioPedido
from .dto import PedidoDTO
from .mapeadores import MapeadorPedido

class ServicioPedido(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_pedido: FabricaPedido = FabricaPedido()
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    def fabrica_pedido(self):
        return self._fabrica_pedido

    def obtener_pedido_por_id(self, id) -> PedidoDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPedido.__class__)
        return self.fabrica_pedido.crear_objeto(repositorio.obtener_por_id(id), MapeadorPedido())