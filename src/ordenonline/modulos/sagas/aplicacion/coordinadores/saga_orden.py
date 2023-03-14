from ordenonline.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from ordenonline.seedwork.aplicacion.comandos import Comando
from ordenonline.seedwork.dominio.eventos import EventoDominio

from ordenonline.modulos.ordenes.aplicacion.comandos.cancelar_orden import CancelarOrden
from ordenonline.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from ordenonline.modulos.ordenes.dominio.eventos.ordenes import OrdenCreada, CreacionOrdenFallida

class CoordinadorOrdenes(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearOrden, evento=OrdenCreada, error=CreacionOrdenFallida, compensacion=CancelarOrden()),
            Fin(index=2)
        ]
    
    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...

    # TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
    def oir_mensaje(mensaje):

        if isinstance(mensaje, EventoDominio):
            coordinador = CoordinadorOrdenes()
            coordinador.procesar_evento(mensaje)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
