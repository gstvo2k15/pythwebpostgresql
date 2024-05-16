# Project Title: pythwebpostgresql
## Overview
This project consists of a Flask application with a PostgreSQL database backend, monitored by Prometheus and Grafana. The application is load balanced and expose using Nginx, and all services are containerized using Docker.


## Basic diagram

```
testapp/
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── blackbox_exporter/
│   └── Dockerfile
├── node_exporter/
│   └── Dockerfile
├── grafana/
│   ├── Dockerfile
│   └── provisioning/
│       └── datasources/
│           └── datasource.yml
├── db/
│   ├── Dockerfile
│   └── init.sql
├── cadvisor/
│   └── Dockerfile
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── prometheus/
│   ├── Dockerfile
│   └── prometheus.yml
└── docker-compose.yml
```


## Summary of technologies used
- Python
- Flask
- PostgreSQL
- Docker
- Prometheus
- Grafana
- Nginx
- Terraform
- GitHub Actions
- GitLab CI
- Azure AKS


## Local Development Setup
### Prerequisites
- Docker
- Docker Compose


## Technologies used locally
- Git: For version control.
- Github: Repository storage of our project.
- Docker/docker-compose: For containerizing applications.
- Nginx: Frontend as a load balancer and reverse proxy of our app.
- PostgreSQL: As the backend database.
- Prometheus: For monitoring and alerting.
- Grafana: Tool for visuale metrics.
- Exporters: Collectors of container metrics about service resources, etc.


### Installation Steps
1. Clone the Repository:
   ```
   git clone https://github.com/gstvo2k15/pythwebpostgresql.git
   cd testapp
   docker-compose up -d
   ```


## Initial steps to performance

We need to create a basic web server using python or js with postgresql backend that counts the number of unique visitors and displays
this statistic:

· "/" - Will be the main page with all data shown.
· "/version" - Will be JSON response with current App version. 


Example output:
```
docker-compose down --remove-orphans
docker-compose build
docker-compose up -d
 
[root@k8smaster testapp]# docker-compose ps
NAME                          COMMAND                  SERVICE             STATUS               PORTS
testapp-app1-1                "flask run --host=0.…"   app1                running              0.0.0.0:5001->5000/tcp, :::5001->5000/tcp
testapp-app2-1                "flask run --host=0.…"   app2                running              0.0.0.0:5002->5000/tcp, :::5002->5000/tcp
testapp-blackbox_exporter-1   "/bin/blackbox_expor…"   blackbox_exporter   running              0.0.0.0:9115->9115/tcp, :::9115->9115/tcp
testapp-cadvisor-1            "/usr/bin/cadvisor -…"   cadvisor            running (starting)   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp
testapp-db-1                  "docker-entrypoint.s…"   db                  running              0.0.0.0:5432->5432/tcp, :::5432->5432/tcp
testapp-grafana-1             "/run.sh"                grafana             running              0.0.0.0:3000->3000/tcp, :::3000->3000/tcp
testapp-nginx-1               "/docker-entrypoint.…"   nginx               running              0.0.0.0:80->80/tcp, :::80->80/tcp
testapp-node_exporter-1       "/bin/node_exporter"     node_exporter       running              0.0.0.0:9100->9100/tcp, :::9100->9100/tcp
testapp-prometheus-1          "/bin/prometheus --c…"   prometheus          running              0.0.0.0:9090->9090/tcp, :::9090->9090/tcp
```


## Main URL check:
```
http://192.168.1.33/
unique_visitors	2


http://192.168.1.33/version
version	"1.0.0"


[root@k8smaster testapp]# docker exec -it testapp-db-1 psql -U postgres -c 'SELECT * FROM visitors;'
 id  |     ip     |         timestamp
-----+------------+----------------------------
 412 | 172.29.0.2 | 2024-05-15 12:09:23.876457
 413 | 172.29.0.2 | 2024-05-15 12:09:35.568058
 414 | 172.29.0.2 | 2024-05-15 12:09:38.876494


[root@k8smaster testapp]# curl -ik http://localhost/
HTTP/1.1 200 OK
Server: nginx/1.26.0
Date: Wed, 15 May 2024 12:10:17 GMT
Content-Type: application/json
Content-Length: 22
Connection: keep-alive

{"unique_visitors":2}
```

## Prometheus URLs:
```
http://192.168.1.33:9090/targets?search=

http://192.168.1.33:5001/metrics

http://192.168.1.33:5002/metrics

http://192.168.1.33:8080/containers/

http://192.168.1.33:9115/metrics

http://192.168.1.33:9100/metrics

http://192.168.1.33:3000/login
```


## How to Upload the Application to the Cloud using CI/CD with GitLab and Deploy it to Azure AKS using Terraform
Prerequisites
```
    GitHub Repository: Contains the source code and configuration files.
    GitLab: Used for CI/CD.
    Azure: For infrastructure deployment.
    Terraform: For infrastructure as code.
    GitLab Runner: To run CI/CD tasks.
```

Steps to Configure the CI/CD Pipeline
```
    Set up Secrets on GitHub:
        Add secrets on GitHub to:
            CI_REGISTRY: GitLab container registry URL.
            CI_REGISTRY_USER: GitLab username.
            CI_REGISTRY_PASSWORD: GitLab password or access token.
            AZURE_CLIENT_ID: Azure client ID.
            AZURE_CLIENT_SECRET: Azure client secret.
            AZURE_SUBSCRIPTION_ID: Azure subscription ID.
            AZURE_TENANT_ID: Azure tenant ID.
```
    Create the .gitlab-ci.yml File on your GitLab repository:
```

```

Create and Configure Terraform Files:
```
    - main.tf: Defines the AKS infrastructure.
    - variables.tf: Defines the variables necessary for the deployment.
    - outputs.tf: Defines the outputs that Terraform should provide.
```
Run the Pipeline:
```
    Push the changes to GitHub, which triggers the GitLab pipeline to build the Docker images and deploy them to AKS using Terraform.
```