#!/bin/bash

# init backend server
cd backend/
sudo apt install libpq-dev
python3 -m venv env
source env/bin/activate

if [ ! -f "requirements.txt" ]; then
  echo "Installing requirements and creating requirements.txt..."
  echo
  pip install wheel
  pip install django
  pip install djangorestframework
  pip install pytest pytest-django pytest-cov mixer
  pip install autopep8
  pip freeze >requirements.txt
else
  echo "Found requirements.txt. Installing requirements..."
  pip install -r requirements.txt
fi

cd django_store_project
python3 manage.py migrate
cd ../..

# init frontend server
cd frontend/
npm install

code ..
