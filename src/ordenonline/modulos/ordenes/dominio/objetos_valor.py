"""Objetos valor del dominio de vuelos

En este archivo usted encontrarĂ¡ los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from enum import Enum



class EstadoOrden(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"