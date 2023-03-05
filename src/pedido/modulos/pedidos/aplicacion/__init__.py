from pydispatch import dispatcher

from .handlers import HandlerPedidoIntegracion

from pedido.modulos.pedidos.dominio.eventos import PedidoCreado

dispatcher.connect(HandlerPedidoIntegracion.handle_pedido_creado, signal=f'{PedidoCreado.__name__}Integracion')