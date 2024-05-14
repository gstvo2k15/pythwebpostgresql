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
│   └── Dockerfile
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
testapp-app1-1               | psycopg2.errors.UndefinedTable: relation "visits" does not exist
testapp-app1-1               | LINE 1: SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;
testapp-db-1                 | 2024-05-14 21:07:44.404 UTC [73] STATEMENT:  SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;
testapp-db-1                 | 2024-05-14 21:07:54.697 UTC [75] ERROR:  relation "visits" does not exist at character 51
testapp-db-1                 | 2024-05-14 21:07:54.697 UTC [75] STATEMENT:  SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;
testapp-db-1                 | 2024-05-14 21:07:59.397 UTC [76] ERROR:  relation "visits" does not exist at character 51
testapp-db-1                 | 2024-05-14 21:07:59.397 UTC [76] STATEMENT:  SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;
testapp-app1-1               |                                                           ^
testapp-app1-1               |
testapp-app1-1               | 172.24.0.2 - - [14/May/2024 21:07:59] "GET / HTTP/1.1" 500 -
testapp-grafana-1            | logger=ngalert.multiorg.alertmanager t=2024-05-14T21:06:13.293232862Z level=info msg="Starting MultiOrg Alertmanager"
testapp-cadvisor-1           | W0514 21:05:48.064678       1 machine_libipmctl.go:64] There are no NVM devices!
testapp-node_exporter-1      | ts=2024-05-14T21:05:47.987Z caller=node_exporter.go:118 level=info collector=watchdog
testapp-node_exporter-1      | ts=2024-05-14T21:05:47.987Z caller=node_exporter.go:118 level=info collector=xfs
testapp-grafana-1            | logger=ticker t=2024-05-14T21:06:13.295108779Z level=info msg=starting first_tick=2024-05-14T21:06:20Z
testapp-grafana-1            | logger=grafana.update.checker t=2024-05-14T21:06:13.447834358Z level=info msg="Update check succeeded" duration=154.180863ms
testapp-grafana-1            | logger=plugins.update.checker t=2024-05-14T21:06:13.464499129Z level=info msg="Update check succeeded" duration=171.951657ms
testapp-grafana-1            | logger=infra.usagestats t=2024-05-14T21:07:48.312549847Z level=info msg="Usage stats are ready to report"
testapp-blackbox_exporter-1  | ts=2024-05-14T21:05:47.859Z caller=main.go:87 level=info msg="Starting blackbox_exporter" version="(version=0.25.0, branch=HEAD, revision=ef3ff4fef195333fb8ee0039fb487b2f5007908f)"
testapp-node_exporter-1      | ts=2024-05-14T21:05:47.987Z caller=node_exporter.go:118 level=info collector=zfs
testapp-node_exporter-1      | ts=2024-05-14T21:05:47.989Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9100
testapp-node_exporter-1      | ts=2024-05-14T21:05:47.989Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9100
testapp-prometheus-1         | ts=2024-05-14T21:05:48.196Z caller=main.go:1153 level=info msg="TSDB started"
testapp-prometheus-1         | ts=2024-05-14T21:05:48.197Z caller=main.go:1335 level=info msg="Loading configuration file" filename=/etc/prometheus/prometheus.yml
testapp-blackbox_exporter-1  | ts=2024-05-14T21:05:47.859Z caller=main.go:88 level=info build_context="(go=go1.22.2, platform=linux/amd64, user=root@47d5b0d99f18, date=20240409-12:58:39, tags=unknown)"
testapp-blackbox_exporter-1  | ts=2024-05-14T21:05:47.861Z caller=main.go:100 level=info msg="Loaded config file"
testapp-blackbox_exporter-1  | ts=2024-05-14T21:05:47.863Z caller=tls_config.go:313 level=info msg="Listening on" address=[::]:9115
testapp-blackbox_exporter-1  | ts=2024-05-14T21:05:47.863Z caller=tls_config.go:316 level=info msg="TLS is disabled." http2=false address=[::]:9115
testapp-prometheus-1         | ts=2024-05-14T21:05:48.200Z caller=main.go:1372 level=info msg="Completed loading of configuration file" filename=/etc/prometheus/prometheus.yml totalDuration=3.107914ms db_storage=15.448µs remote_storage=4.915µs web_handler=943ns query_engine=2.571µs scrape=1.028706ms scrape_sd=532.764µs notify=2.607µs notify_sd=3.072µs rules=15.823µs tracing=133.198µs
testapp-prometheus-1         | ts=2024-05-14T21:05:48.200Z caller=main.go:1114 level=info msg="Server is ready to receive web requests."
testapp-prometheus-1         | ts=2024-05-14T21:05:48.200Z caller=manager.go:163 level=info component="rule manager" msg="Starting rule manager..."
testapp-nginx-1              | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
testapp-nginx-1              | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
testapp-nginx-1              | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
testapp-nginx-1              | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
testapp-nginx-1              | /docker-entrypoint.sh: Configuration complete; ready for start up
testapp-app2-1               | psycopg2.errors.UndefinedTable: relation "visits" does not exist
testapp-app2-1               | LINE 1: SELECT COUNT(DISTINCT ip) AS unique_visitors FROM visits;
testapp-app2-1               |                                                           ^
testapp-app2-1               |
testapp-app2-1               | 172.24.0.2 - - [14/May/2024 21:07:54] "GET / HTTP/1.1" 500 -
testapp-app2-1               | 172.24.0.5 - - [14/May/2024 21:08:08] "GET /metrics HTTP/1.1" 404 -
```
