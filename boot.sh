#!/bin/bash

source venv/bin/activate
#flask deploy
exec gunicorn -b 0.0.0.0:80 --access-logfile - --error-logfile - flask_blog:app
#/bin/bash