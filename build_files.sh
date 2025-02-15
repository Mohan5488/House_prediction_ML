#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
if command -v python3.9 &>/dev/null; then
    python3.9 manage.py collectstatic --noinput
elif command -v python3 &>/dev/null; then
    python3 manage.py collectstatic --noinput
else
    python manage.py collectstatic --noinput
fi
