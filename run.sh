#! /bin/bash
# Executes the Python flask app on a production web server

source venv/bin/activate
gunicorn --workers=2 -b 0.0.0.0:8000 --pythonpath src app:app --log-level debug