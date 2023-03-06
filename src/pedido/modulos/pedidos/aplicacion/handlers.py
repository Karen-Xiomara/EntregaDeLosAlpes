from pedido.modulos.pedidos.dominio.eventos import PedidoCreado
from pedido.seedwork.aplicacion.handlers import Handler
from pedido.modulos.pedidos.infraestructura.despachadores import Despachador

class HandlerPedidoIntegracion(Handler):

    @staticmethod
    def handle_pedido_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-pedido')    