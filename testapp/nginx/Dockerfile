# Utiliza la imagen base de nginx
FROM nginx:stable-alpine

# Copia tu configuración personalizada de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copia el script de espera
COPY wait-for-it.sh /wait-for-it.sh

# Asegúrate de que el script es ejecutable
RUN chmod +x /wait-for-it.sh

# Instala nc (netcat)
RUN apk --no-cache add netcat-openbsd

# Crear directorios para logs y asegurar permisos
RUN mkdir -p /var/log/nginx && \
    chmod -R 755 /var/log/nginx && \
    touch /var/log/nginx/access.log /var/log/nginx/error.log && \
    chmod 666 /var/log/nginx/*.log

# Comando para ejecutar el script de espera y luego iniciar Nginx
CMD ["/wait-for-it.sh", "code_checker", "nginx", "-g", "daemon off;"]

