@echo off
REM Setup virtual environment
python -m venv env

REM Activate environment (Windows)
call env\Scripts\activate

REM Install required packages
pip install django djangorestframework requests

REM Start Django project and app
django-admin startproject weather_project .
python manage.py startapp weather

REM Create project folders
mkdir weather\management
mkdir weather\management\commands
mkdir weather\migrations
mkdir static
mkdir templates
mkdir data

REM Create placeholder files
echo.> weather\serializers.py
echo.> weather\urls.py
echo.> weather\management\__init__.py
echo.> weather\management\commands\__init__.py
echo.> weather\tests.py

REM Notify user
echo Project structure created!