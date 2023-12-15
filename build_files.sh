#!/bin/bash

echo "BUILD START"

# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3.9 python3.9-venv cmake

# Create virtual environment
python3.9 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt

# Run Django migrations (assuming your project has database migrations)
python manage.py migrate

echo "BUILD END"
