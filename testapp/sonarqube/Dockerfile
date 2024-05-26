# Usa la última imagen de Alpine como base
FROM alpine:latest

# Instalar dependencias necesarias
RUN apk update && apk add --no-cache \
    openjdk11-jre \
    wget \
    unzip \
    curl \
    jq \
    bash

# Descargar e instalar SonarQube
RUN wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.5.0.56709.zip \
    && unzip sonarqube-9.5.0.56709.zip -d /opt \
    && mv /opt/sonarqube-9.5.0.56709 /opt/sonarqube \
    && rm sonarqube-9.5.0.56709.zip

# Descargar e instalar SonarScanner
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip \
    && unzip sonar-scanner-cli-4.6.2.2472-linux.zip -d /opt \
    && rm sonar-scanner-cli-4.6.2.2472-linux.zip

# Añadir SonarScanner al PATH
ENV PATH="/opt/sonar-scanner-4.6.2.2472-linux/bin:${PATH}"

# Copiar el script de inicio al directorio de SonarQube
COPY start-sonarqube.sh /opt/sonarqube/start-sonarqube.sh

# Dar permisos de ejecución al script
RUN chmod +x /opt/sonarqube/start-sonarqube.sh

# Definir el punto de entrada
ENTRYPOINT ["/opt/sonarqube/start-sonarqube.sh"]

