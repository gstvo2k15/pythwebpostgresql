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

