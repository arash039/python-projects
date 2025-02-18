# Life Pro Tips

Life Pro Tips is a Django-based web application where users can share, upvote, and downvote life tips. Users can register, log in, and manage their tips. The application also features a reputation system based on user interactions with tips.

## Features

- User registration and authentication
- Share life tips
- Upvote and downvote tips
- Delete tips
- User reputation system
- Responsive design using Bootstrap

## Technologies Used

- **Models**: The application uses Django's ORM to define models for users and tips. The `Tip` model includes fields for the tip content, author, and vote counts. The `CustomUser` model extends Django's built-in user model to include additional fields like reputation.
  
- **Forms**: Django forms are used for user registration, login, and tip submission. The forms handle validation and rendering, making it easy to create and process HTML forms.

- **Views**: The application uses class-based views to handle requests and return responses. Views are responsible for rendering templates and processing form data.

- **Templates**: Django's templating engine is used to create dynamic HTML pages. Templates are used to render the home page, login page, registration page, and other parts of the application.

### Custom User Model

The application uses a custom user model to extend the default Django user model. This allows for additional fields and methods specific to the application's needs. The `CustomUser` model includes a reputation field that tracks the user's reputation based on the votes their tips receive. This reputation allows user to vote down the tips or delete them after reaching certain level of reputation.

### Bootstrap

Bootstrap is a popular front-end framework for building responsive, mobile-first websites. The application uses Bootstrap to ensure a consistent and responsive design across different devices. Bootstrap components and utilities are used for layout, forms, buttons, and other UI elements.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/lifeprotips.git
    cd lifeprotips
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).

## Usage

- Register a new user or log in with an existing account.
- Share your life tips on the home page.
- Upvote or downvote tips shared by other users.
- Delete your own tips if necessary.
- Monitor your reputation based on the interactions with your tips.

