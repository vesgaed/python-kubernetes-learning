# PASO 1: Usar una imagen base oficial de Python. Es ligera y optimizada.
FROM python:3.9-slim

# PASO 2: Establecer el directorio de trabajo dentro de la imagen.
WORKDIR /app

# PASO 3: Copiar solo el archivo de requisitos e instalarlos.
# Docker guarda en caché este paso. Si no cambiamos los requisitos, no se volverá a ejecutar, haciendo las builds más rápidas.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# PASO 4: Copiar el resto del código de nuestra aplicación.
COPY . .

# PASO 5: Comando que se ejecutará cuando el contenedor se inicie.
CMD ["python", "app.py"]