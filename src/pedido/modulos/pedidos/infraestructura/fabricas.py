from dataclasses import dataclass, field
from pedido.seedwork.dominio.fabricas import Fabrica
from pedido.seedwork.dominio.repositorios import Repositorio
from pedido.modulos.pedidos.dominio.repositorios import RepositorioPedido
from .repositorios import RepositorioPedidoSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPedido.__class__:
            return RepositorioPedidoSQLite()
        else:
            raise ExcepcionFabrica()