#!/bin/bash

# Formatear el código con autopep8
autopep8 --in-place --aggressive --aggressive /app/app.py

# Ejecutar Pylint
pylint --rcfile=/app/.pylintrc /app/app.py

