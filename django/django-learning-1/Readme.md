# Django Learing Project 1

This project is a Django-based web application. It is organized into multiple Django apps, each with its own functionality.

## Project Apps

- **d05**: Main Django project configuration.
- **ex00**: This app contains basic functionalities and serves as the starting point for the project.
- **ex01**: This app demonstrates more advanced Django features such as static files and templates.
- **ex02**: This app demonstrates creating a simple form using django.forms.Form class and showing the form submission history
- **ex03**: This app generates and displays a table of progressively lighter color shades (black, red, blue, and green) using Django, dynamically rendering RGB values in an HTML template.


## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd ex00
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations and collect static files:**

    ```sh
    python manage.py migrate
	python manage.py collectstatic
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```


