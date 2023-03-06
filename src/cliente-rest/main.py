import os, requests, logging

class OrdenOnline():
    HOSTNAME_ENV: str = 'ordenonline'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5000'
    REST_API_ENDPOINT: str = '/ordenes/orden-comando'

    def CrearOrden(self):
        dict_obj = {"fecha_creacion": "25/05/2002",
                    "fecha_actualizacion": "25/05/2003",
                    "id": "401"}

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 200:
            return "OK"
        else:
            return "FAILED"


def run():
    orden_cliente = OrdenOnline()
    orden_cliente.CrearOrden()

if __name__ == '__main__':
    logging.basicConfig()
    run()