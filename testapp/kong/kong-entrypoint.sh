#!/bin/sh

# Esperar a que la base de datos de Kong esté lista
until nc -z -v -w30 db 5432
do
  echo "Esperando a que la base de datos de Kong esté disponible..."
  sleep 1
done

# Ejecutar las migraciones de Kong y arrancar el servicio
kong migrations bootstrap
kong start

# Importar la configuración de Kong
kong config db_import /kong/kong.yml

# Mantener el contenedor en ejecución
tail -f /dev/null

