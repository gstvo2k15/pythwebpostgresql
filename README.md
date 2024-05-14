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

Errors showed:
```
[root@k8smaster testapp]# docker-compose logs -f --tail=5
[root@k8smaster testapp]# docker-compose logs -f --tail=5
testapp-node_exporter-1      | ts=2024-05-14T21:17:29.394Z caller=node_exporter.go:118 level=info collector=watchdog
testapp-node_exporter-1      | ts=2024-05-14T21:17:29.394Z caller=node_exporter.go:118 level=info collector=xfs
testapp-node_exporter-1      | ts=2024-05-14T21:17:29.394Z caller=node_exporter.go:118 level=info collector=zfs
testapp-node_exporter-1      | ts=2024-05-14T21:17:29.396Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9100
testapp-node_exporter-1      | ts=2024-05-14T21:17:29.396Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9100
testapp-cadvisor-1           | W0514 21:17:29.334967       1 machine_libipmctl.go:64] There are no NVM devices!
testapp-db-1                 | 2024-05-14 21:17:33.801 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
testapp-db-1                 | 2024-05-14 21:17:33.801 UTC [1] LOG:  listening on IPv6 address "::", port 5432
testapp-db-1                 | 2024-05-14 21:17:33.832 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
testapp-db-1                 | 2024-05-14 21:17:33.878 UTC [50] LOG:  database system was shut down at 2024-05-14 21:17:33 UTC
testapp-db-1                 | 2024-05-14 21:17:33.911 UTC [1] LOG:  database system is ready to accept connections
testapp-app2-1               | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
testapp-app2-1               |  * Running on all addresses (0.0.0.0)
testapp-app2-1               |  * Running on http://127.0.0.1:5000
testapp-app2-1               |  * Running on http://172.25.0.9:5000
testapp-app1-1               | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
testapp-app2-1               | Press CTRL+C to quit
testapp-app1-1               |  * Running on all addresses (0.0.0.0)
testapp-app1-1               |  * Running on http://127.0.0.1:5000
testapp-app1-1               |  * Running on http://172.25.0.8:5000
testapp-app1-1               | Press CTRL+C to quit
testapp-grafana-1            | logger=migrator t=2024-05-14T21:17:37.390579497Z level=info msg="Executing migration" id="Add index for created in annotation table"
testapp-grafana-1            | logger=migrator t=2024-05-14T21:17:37.420349657Z level=info msg="Executing migration" id="Add index for updated in annotation table"
testapp-grafana-1            | logger=migrator t=2024-05-14T21:17:37.447461447Z level=info msg="Executing migration" id="Convert existing annotations from seconds to milliseconds"
testapp-nginx-1              | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
testapp-nginx-1              | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
testapp-nginx-1              | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
testapp-nginx-1              | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
testapp-grafana-1            | logger=migrator t=2024-05-14T21:17:37.473012194Z level=info msg="Executing migration" id="Add epoch_end column"
testapp-grafana-1            | logger=migrator t=2024-05-14T21:17:37.510472204Z level=info msg="Executing migration" id="Add index for epoch_end"
testapp-nginx-1              | /docker-entrypoint.sh: Configuration complete; ready for start up
testapp-prometheus-1         | ts=2024-05-14T21:17:29.265Z caller=main.go:1153 level=info msg="TSDB started"
testapp-prometheus-1         | ts=2024-05-14T21:17:29.265Z caller=main.go:1335 level=info msg="Loading configuration file" filename=/etc/prometheus/prometheus.yml
testapp-prometheus-1         | ts=2024-05-14T21:17:29.268Z caller=main.go:1372 level=info msg="Completed loading of configuration file" filename=/etc/prometheus/prometheus.yml totalDuration=3.461699ms db_storage=3.297µs remote_storage=3.789µs web_handler=1.128µs query_engine=2.549µs scrape=1.265637ms scrape_sd=870.41µs notify=2.852µs notify_sd=2.994µs rules=4.655µs tracing=30.155µs
testapp-prometheus-1         | ts=2024-05-14T21:17:29.268Z caller=main.go:1114 level=info msg="Server is ready to receive web requests."
```

URL check:
```
http://192.168.1.33/
unique_visitors	3


http://192.168.1.33/version
version	"1.0.0"


[root@k8smaster testapp]# docker exec -it testapp-db-1 psql -U postgres -c 'SELECT * FROM visits;'
 id | ip | timestamp
----+----+-----------
(0 rows)

[root@k8smaster testapp]#
[root@k8smaster testapp]# docker exec -it testapp-db-1 psql -U postgres -c 'SELECT DISTINCT ip FROM visits;'
 ip
----
(0 rows)

```
