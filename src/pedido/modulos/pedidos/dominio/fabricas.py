from dataclasses import dataclass
from pedido.seedwork.dominio.repositorios import Mapeador
from pedido.seedwork.dominio.fabricas import Fabrica
from pedido.seedwork.dominio.entidades import Entidad
from .entidades import Pedido
from .excepciones import TipoObjetoNoExisteEnDominioPedidoExcepcion

@dataclass
class _FabricaPedido(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            pedido: Pedido = mapeador.dto_a_entidad(obj)
            return pedido

@dataclass
class FabricaPedido(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Pedido.__class__:
            fabrica = _FabricaPedido()
            return fabrica.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPedidoExcepcion()
