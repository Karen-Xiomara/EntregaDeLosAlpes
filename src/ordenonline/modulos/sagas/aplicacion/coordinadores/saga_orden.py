from ordenonline.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from ordenonline.seedwork.aplicacion.comandos import Comando
from ordenonline.seedwork.dominio.eventos import EventoDominio
from ordenonline.modulos.ordenes.aplicacion.comandos.cancelar_orden import CancelarOrden
from ordenonline.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from ordenonline.modulos.ordenes.dominio.eventos import OrdenCreada, CreacionOrdenFallida

class CoordinadorOrdenes(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        print("ha ingresado a inicializar los pasos")
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1,comando=CrearOrden, evento=OrdenCreada, error=CreacionOrdenFallida, compensacion=CancelarOrden, exitosa=None),
            Fin(index=2)
        ]
    
    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        ...

    @classmethod
    def oir_mensaje(cls, mensaje):
        if isinstance(mensaje, EventoDominio):
            print("ha ingresado a oir_mensaje")
            coordinador = CoordinadorOrdenes()
            coordinador.procesar_evento(mensaje)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
