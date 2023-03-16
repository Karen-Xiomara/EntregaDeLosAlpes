# Entrega de los Alpes

## Estructura del proyecto

Los siguientes son los microservicios implementados:

- **cliente-rest** en este directorio se encuentra el cliente rest para realizar la peticion al microservicio de Ordenonlie.
- **notificaciones** en este directorio se encuentra el microservicio de notificaciones, el cual se subscribe al topico **eventos-pedido**
- **ordenonline** en este directorio se encuentra el microservicio de Ordenesonline, el cual recibe una orden la cual es almacenada en base datos, para luego publicar en el topico de **eventos-orden** 
- **pedido** en este directorio se encuentra el microservicio de Pedidos, el cual se subscribe al topico de **eventos-orden** para recibir una orden la cual es almacenada en base datos para luego publicar en el topico de **eventos-pedido**
- **ui** en este directorio se encuentra el microservicio de interfaz web, este micro se subscribe al topico **eventos-orden** para mostrar el contenido del mensaje en una interfaz html. 
- **bff** en este directorio se encuentra el backend for frontend, el cual publica en el tópico **comandos-orden** que inicia el proceso de creación de una orden 


### Ejecutar Aplicación

* Iniciar el servicio de Pulsar.
```bash
docker-compose --profile pulsar up
```

* Iniciar el microservicio de Ordenes Online:
```bash
flask --app src/ordenonline/api --debug run
```

* Iniciar el microservicio de Pedidos:
```bash
flask --app src/pedido/api --debug run -p 5001
```

* Iniciar el microservicio de Notificaciones:
```bash
python src/notificaciones/main.py

```

* Iniciar el BFF:
```bash
pip install -r bff-requirements.txt
cd src
uvicorn bff_web.main:app --host localhost --port 8003 --reload

```



* Iniciar el microservicio de UI:
```bash
python src/ui/main.py
```

* Ejecutar el cliente rest:
```bash
python src/cliente-rest/main.py
```


## Probar el endpoint del BFF
Se debe subir los contenedores de pulsar, subir el ms ordenonline, ms pedido, ms notificaciones, ms notificaciones y el BFF. Se debe habilitar el puerto del BFF como público y acceder a la url generada en la pestaña de PORTS que comienza con con el puerto  8003.... Por último en la raiz del proyecto se encuentra la colección postman de nombre Nomonoliticas.postman_collection.json que se pueda usar para hacer la solicitud usando GraphQL


