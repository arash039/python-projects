# Django Learning Project 2
## Overview
This workspace contains solutions to various Django exercises and projects, covering topics such as database modeling, views, templates, and forms.

## Directory Structure
The workspace is organized into the following directories:

- **d05**: The main Django project directory, containing the project settings, apps, and templates.
- **ex00-ex10**: Individual exercise directories, each containing a specific Django app with its own models, views, templates, and forms.
- **resources**: A directory containing additional resources, such as JSON data files and PostgreSQL scripts.

## Exercise Descriptions
Each exercise directory (ex00-ex10) contains a specific Django app with its own models, views, templates, and forms. The exercises cover a range of topics, including:

- **ex00**: Creating a simple Django app with a single model and view.
- **ex01**: Creating a Django app with multiple models and views.
- **ex02**: Using Django forms to validate user input.
- **ex03**: Creating a Django app with a many-to-many relationship between models.
- **ex04**: Using Django templates to render dynamic content.
- **ex05**: Creating a Django app with a custom admin interface.
- **ex06**: Using Django's built-in authentication and authorization system.
- **ex07**: Creating a Django app with a custom authentication system.
- **ex08**: Using Django's built-in caching system.
- **ex09**: Creating a Django app with a custom caching system.
- **ex10**: Creating a Django app with a complex data model and multiple relationships.

## Running the Exercises
To run each exercise, navigate to the corresponding directory and execute the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
This will start the Django development server, and you can access the exercise app by visiting http://localhost:8000/exXX/ in your web browser.
