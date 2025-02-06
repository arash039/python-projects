# Django Learning Project 2

This project aims to provide hands-on experience with Django's Object-Relational Mapping (ORM) and SQL. Each exercise focuses on different aspects of Django models, views, and database interactions. Below is a description of each exercise.

## Exercises

### Exercise 00 - SQL: Building a Table
- **Description**: Create a Django application named `ex00` with a view accessible at `127.0.0.1:8000/ex00/init`. This view should create an SQL table in PostgreSQL using the `psycopg2` library and return "OK" if successful or an error message if not.
- **Table Specifications**: `ex00_movies`
  - `title`: unique, VARCHAR(64), non-null
  - `episode_nb`: int, PRIMARY KEY
  - `opening_crawl`: text, nullable
  - `director`: VARCHAR(32), non-null
  - `producer`: VARCHAR(128), non-null
  - `release_date`: date, non-null

### Exercise 01 - ORM: Building a Table
- **Description**: Create a Django application named `ex01` with a model named `Movies`. The model should have fields for `title`, `episode_nb`, `opening_crawl`, `director`, `producer`, and `release_date`, and should redefine the `__str__` method to return the title attribute.

### Exercise 02 - SQL: Data Insertion
- **Description**: Create a Django application named `ex02` with views accessible at `127.0.0.1:8000/ex02/init`, `127.0.0.1:8000/ex02/populate`, and `127.0.0.1:8000/ex02/display`. These views should create a table, insert specified data, and display the data in an HTML table, respectively.
- **Table Specifications**: `ex02_movies` (same as `ex00_movies`)
- **Data to Insert**: A list of movies with fields for `episode_nb`, `title`, `director`, `producer`, and `release_date`.

### Exercise 03 - ORM: Data Insertion
- **Description**: Create a Django application named `ex03` with a model identical to `ex01` and views accessible at `127.0.0.1:8000/ex03/populate` and `127.0.0.1:8000/ex03/display`. These views should insert specified data into the model and display the data in an HTML table.
- **Model Specifications**: `Movies` (same as `ex01`)

### Exercise 04 - SQL: Data Deletion
- **Description**: Create a Django application named `ex04` with views accessible at `127.0.0.1:8000/ex04/init`, `127.0.0.1:8000/ex04/populate`, `127.0.0.1:8000/ex04/display`, and `127.0.0.1:8000/ex04/remove`. These views should create a table, insert data, display data, and remove data based on user input.
- **Table Specifications**: `ex04_movies` (same as `ex00_movies`)

### Exercise 05 - ORM: Data Deletion
- **Description**: Create a Django application named `ex05` with a model identical to `ex01` and views accessible at `127.0.0.1:8000/ex05/populate`, `127.0.0.1:8000/ex05/display`, and `127.0.0.1:8000/ex05/remove`. These views should insert data, display data, and remove data based on user input.
- **Model Specifications**: `Movies` (same as `ex01`)

### Exercise 06 - SQL: Updating Data
- **Description**: Create a Django application named `ex06` with views accessible at `127.0.0.1:8000/ex06/init`, `127.0.0.1:8000/ex06/populate`, `127.0.0.1:8000/ex06/display`, and `127.0.0.1:8000/ex06/update`. These views should create a table, insert data, display data, and update data based on user input.
- **Table Specifications**: `ex06_movies` (same as `ex00_movies` with additional `created` and `updated` datetime fields)

### Exercise 07 - ORM: Updating Data
- **Description**: Create a Django application named `ex07` with a model identical to `ex01` with additional `created` and `updated` fields, and views accessible at `127.0.0.1:8000/ex07/populate`, `127.0.0.1:8000/ex07/display`, and `127.0.0.1:8000/ex07/update`. These views should insert data, display data, and update data based on user input.
- **Model Specifications**: `Movies` (same as `ex01` with additional `created` and `updated` fields)

### Exercise 08 - SQL: Foreign Key
- **Description**: Create a Django application named `ex08` with views accessible at `127.0.0.1:8000/ex08/init`, `127.0.0.1:8000/ex08/populate`, and `127.0.0.1:8000/ex08/display`. These views should create two tables with a foreign key relationship, insert data, and display the data.
- **Table Specifications**:
  - `ex08_planets`
  - `ex08_people` (with foreign key referencing `ex08_planets`)

### Exercise 09 - ORM: Foreign Key
- **Description**: Create a Django application named `ex09` with two models (`Planets` and `People`) with a foreign key relationship, and views accessible at `127.0.0.1:8000/ex09/display`. The view should display data based on the foreign key relationship.
- **Model Specifications**:
  - `Planets`
  - `People` (with foreign key referencing `Planets`)

### Exercise 10 - ORM: Many to Many
- **Description**: Create a Django application named `ex10` with three models (`Planets`, `People`, and `Movies`) with many-to-many relationships, and a view accessible at `127.0.0.1:8000/ex10`. The view should display data based on the relationships.
- **Model Specifications**:
  - `Planets` (same as `ex09`)
  - `People` (same as `ex09`)
  - `Movies` (same as `ex01` with a many-to-many field for `People`)

## How to Run
1. Clone the repository to your local machine.
2. Navigate to each exercise directory and follow the instructions to set up and run the Django server.
3. Access the views using the specified URLs.

## Requirements
- Python 3.x
- Django
- PostgreSQL
- psycopg2 library

