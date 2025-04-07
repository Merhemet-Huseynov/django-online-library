#!/bin/bash

cd library || exit 1
celery -A library worker --loglevel=info