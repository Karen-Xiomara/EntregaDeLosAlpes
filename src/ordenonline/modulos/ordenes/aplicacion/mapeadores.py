from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import OrdenDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO(externo.get('fecha_creacion'),externo.get('fecha_actualizacion'),externo.get('id') )
        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__
