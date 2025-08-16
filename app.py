from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
# La variable 'REDIS_HOST' la definiremos fuera de nuestro código.
# Docker Compose se la proporcionará a nuestro contenedor.
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis = Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    # 'incr' es un comando de Redis que incrementa un valor. Si no existe, lo crea en 1.
    count = redis.incr('hits')
    # Obtenemos el "hostname", que dentro de un contenedor es su ID único.
    # Esto nos ayudará a ver el balanceo de carga más adelante.
    hostname = socket.gethostname()
    return f"<h1>Contador de Visitas</h1><p>Esta página ha sido visitada <strong>{count}</strong> veces.</p><p><i>Servido por el contenedor: {hostname}</i></p>"

if __name__ == "__main__":
    # Escucha en todas las interfaces de red dentro del contenedor
    app.run(host="0.0.0.0", port=5000)