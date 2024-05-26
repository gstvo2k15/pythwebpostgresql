# Utiliza la imagen base de Python 3.9 en Alpine
FROM python:3.9-alpine

# Establece la variable de entorno para que no genere archivos pyc
ENV PYTHONUNBUFFERED=1

# Instala dependencias necesarias
RUN apk update && \
    apk add --no-cache gcc musl-dev linux-headers git

# Instala pylint, autopep8 y Flask
RUN pip install --upgrade pip && \
    pip install pylint autopep8 Flask prometheus_flask_exporter

# Crea el directorio de trabajo
WORKDIR /app

# Copia el contenido del directorio app al directorio de trabajo
COPY ../app /app

# Comando para ejecutar el servidor Flask
CMD ["python3", "app.py"]

