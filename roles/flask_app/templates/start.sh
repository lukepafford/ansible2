#!/bin/bash
source /var/anaconda/bin/activate flask_app
gunicorn -c gunicorn_config flask_app:app
