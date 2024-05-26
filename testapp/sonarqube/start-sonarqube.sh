#!/bin/bash

# Listar el contenido de /opt/sonarqube/
ls -ltrR /opt/sonarqube/

# Buscar el archivo sonar.sh en el directorio de SonarQube
SONAR_SH_PATH=$(find /opt/sonarqube -name sonar.sh | grep 'linux-x86-64')

if [ -z "$SONAR_SH_PATH" ]; then
  echo "sonar.sh no encontrado en /opt/sonarqube/"
  exit 1
else
  echo "sonar.sh encontrado en $SONAR_SH_PATH"
fi

# Iniciar SonarQube en segundo plano
$SONAR_SH_PATH start

# Esperar a que SonarQube se inicie completamente
echo "Esperando a que SonarQube se inicie..."
until curl -s http://localhost:9000/api/system/status | grep -q '"status":"UP"'; do
  sleep 5
done
echo "SonarQube está en funcionamiento."

# Generar un nuevo token de autenticación usando la API de SonarQube
echo "Generando token de autenticación..."
TOKEN_RESPONSE=$(curl -u admin:admin -X POST 'http://localhost:9000/api/user_tokens/generate' -d "name=automation-token")
NEW_TOKEN=$(echo $TOKEN_RESPONSE | jq -r '.token')

if [ "$NEW_TOKEN" != "null" ]; then
  echo "Nuevo token generado: $NEW_TOKEN"
else
  echo "Error al generar el token. Respuesta de la API:"
  echo $TOKEN_RESPONSE
  exit 1
fi

# Ejecutar SonarScanner en el proyecto especificado
echo "Ejecutando SonarScanner..."
/opt/sonar-scanner-4.6.2.2472-linux/bin/sonar-scanner \
  -Dsonar.projectKey=pythweb \
  -Dsonar.sources=/mnt/code \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=$NEW_TOKEN

# Mantener el contenedor en ejecución para ver los logs
tail -f /opt/sonarqube/logs/sonar.log

