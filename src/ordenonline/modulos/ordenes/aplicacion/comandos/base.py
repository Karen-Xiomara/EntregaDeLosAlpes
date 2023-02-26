from ordenonline.seedwork.aplicacion.comandos import ComandoHandler
from ordenonline.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from ordenonline.modulos.vuelos.dominio.fabricas import FabricaVuelos

class CrearOrdenBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    
    