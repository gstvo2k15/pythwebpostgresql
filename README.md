# pythwebpostgresql
Basic python web server deployment in docker-compose with postgresql backend

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


Main URL check:
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



Prometheus URLs:
```
http://192.168.1.33:9090/targets?search=

http://192.168.1.33:5001/metrics

http://192.168.1.33:5002/metrics

http://192.168.1.33:8080/containers/

http://192.168.1.33:9115/metrics

http://192.168.1.33:9100/metrics

http://192.168.1.33:3000/login
```

## Technologies used locally

- Git: For version control.
- Github: Repository storage of our project.
- Docker/docker-compose: For containerizing applications.
- Nginx: Frontend as a load balancer and reverse proxy of our app.
- PostgreSQL: As the backend database.
- Prometheus: For monitoring and alerting.
- Grafana: Tool for visuale metrics.
- Exporters: Collectors of container metrics about service resources, etc.


