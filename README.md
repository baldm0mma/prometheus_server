A quick and dirty python3 sever that emits metrics for collection via Prometheus.

Clone repo.

Inside of `prometheus_server` directory, run the following to spin up the python3 mock metrics server:

```
python mock_server.py
```

Then, to spin up Prometheus via Docker, run the following:

```
docker-compose up -d
```

Connect to Prometheus via port 9090.
