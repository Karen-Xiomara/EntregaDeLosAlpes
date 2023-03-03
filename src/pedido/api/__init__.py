import os, logging

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio baseapp.logger.info("Texto Id: ")
basedir = os.path.abspath(os.path.dirname(__file__))

### Models Alchemy
def importar_modelos_alchemy():
    import pedido.modulos.pedidos.infraestructura.dto

### Subscripcion a Pulsar
def comenzar_consumidor():
    import threading
    import pedido.modulos.pedidos.infraestructura.consumidores as pedidos

    ### Subscripcion eventos
    threading.Thread(target=pedidos.suscribirse_a_eventos).start()

    ### Subscripcion comandos
    threading.Thread(target=pedidos.suscribirse_a_comandos).start()

### App Flask
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    logging.basicConfig(level=logging.DEBUG)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from pedido.config.db import init_db
    init_db(app)

    from pedido.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

     # Importa Blueprints
    from . import pedidos

    # Registro de Blueprints
    app.register_blueprint(pedidos.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Pedidos API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app