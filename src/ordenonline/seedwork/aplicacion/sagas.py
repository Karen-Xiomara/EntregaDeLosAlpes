from abc import ABC, abstractmethod
from ordenonline.seedwork.aplicacion.comandos import Comando
from ordenonline.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
from .comandos import ejecutar_commando
import uuid
import datetime


class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio, tipo_comando: type) -> Comando:
        ...

    def publicar_comando(self, evento: EventoDominio, tipo_comando: type):
        comando = self.construir_comando(evento, tipo_comando)
        ejecutar_commando(comando)

    @abstractmethod
    def inicializar_pasos(self):
        ...
    
    @abstractmethod
    def procesar_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def iniciar(self):
        ...
    
    @abstractmethod
    def terminar(self):
        ...

class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int

@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    index: int
    ...

@dataclass
class Transaccion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio
    error: EventoDominio
    compensacion: Comando
    exitosa: bool

class CoordinadorCoreografia(CoordinadorSaga, ABC):
    # TODO Piense como podemos hacer un Coordinador con coreografía y Sagas
    # Piense en como se tiene la clase Transaccion, donde se cuenta con un atributo de compensación
    # ¿Tal vez un manejo de tuplas o diccionarios?
    ...

class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: 'list[Paso]'
    index: int
    
    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
                
    def es_ultima_transaccion(self, index):
        return len(self.pasos) - 1

    def procesar_evento(self, evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        print("ha ingresado a procesar evento")
        print(self.es_ultima_transaccion(index))
        print(isinstance(evento, paso.error))
        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):         
            print("ha ingresado a terminar")
            self.terminar()
        elif isinstance(evento, paso.error):
            self.publicar_comando(evento, self.pasos[index-1].compensacion)
            print("ha ingresado publicar comando")
        elif isinstance(evento, paso.evento):
            print("ha ingresado a publicar evento")
            self.publicar_comando(evento, self.pasos[index+1].compensacion)