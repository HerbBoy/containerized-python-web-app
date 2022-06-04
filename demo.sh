#!/bin/bash
# Leveraging gunicorn as the application server (recommended solution over default provided by flask)
exec gunicorn --certfile cert.pem --keyfile key.pem --chdir demo  -b :5000 app:demo