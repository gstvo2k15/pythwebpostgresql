# Utiliza la imagen base de nginx
FROM nginx:stable-alpine

# Copia tu configuración personalizada de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copia el script de espera
COPY wait-for-it.sh /wait-for-it.sh

# Asegúrate de que el script es ejecutable
RUN chmod +x /wait-for-it.sh

# Comando para ejecutar el script de espera y luego iniciar Nginx
CMD ["/wait-for-it.sh", "code_checker", "nginx", "-g", "daemon off;"]

