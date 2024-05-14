# pythwebpostgresql
Basic python web server deployment in docker-compose with postgresql backend

## Basic diagram

```
testapp/
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── db/
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── datasource.yml
└── docker-compose.yml
```

## Initial steps to performance

We need to create a basic web server using python or js with postgresql backend that counts the number of unique visitors and displays
this statistic:

· "/" - Will be the main page with all data shown.
· "/version" - Will be JSON response with current App version. 

