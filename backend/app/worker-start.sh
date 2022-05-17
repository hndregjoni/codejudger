#! /usr/bin/env bash
set -e

# ENV vars
set -a
source /app/.env

python /app/app/celeryworker_pre_start.py

celery worker -A app.worker -l info -Q main-queue -c 1
