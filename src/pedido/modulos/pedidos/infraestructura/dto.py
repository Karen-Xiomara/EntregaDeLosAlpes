from pedido.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    id_client = db.Column(db.String, nullable=False)
    fecha_orden = db.Column(db.String, nullable=False)
    numero_orden = db.Column(db.String, nullable=False)