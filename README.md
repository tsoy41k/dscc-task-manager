# DSCC Task Manager

## Project Description

This project is a web application "Task manager" developed using the **Django framework**.
The application allows users to register, log in, and manage their personal tasks. Each user can create, update, and delete tasks that are stored in a PostgreSQL database.

The system demonstrates the use of modern DevOps practices including **Docker containerization, CI/CD automation with GitHub Actions, and cloud deployment**.



## Features

The application provides the following functionality:

* User registration
* User login and logout
* Create new tasks
* View a list of personal tasks
* Update existing tasks
* Delete tasks
* User-specific task management
* Admin panel for database management



## Technologies Used

The project was built using the following technologies:

* **Python**
* **Django**
* **PostgreSQL**
* **Docker**
* **Docker Compose**
* **GitHub Actions (CI/CD)**
* **Docker Hub**
* **Render Cloud Platform**
* **Bootstrap (UI styling)**



## System Architecture

The application follows Django's **Model-View-Template (MVT)** architecture.

### Models

Models define the database structure and represent the application's core data.

Main model:

* Task

Relationships implemented:

* Many-to-one relationship between **Task and User**
* Many-to-many relationship between **Task and Tags**



### Views

Views handle the application logic and user requests.

Main views implemented:

* Task list view
* Create task view
* Update task view
* Delete task view
* User registration view

All task operations are protected using Django authentication.



### Templates

Templates generate the user interface using Django template engine and HTML.

Main pages include:

* Task list page
* Create task page
* Update task page
* Login page
* Registration page

A **base template** is used to share common layout and navigation elements across pages.



## Docker Containerization

The application is containerized using Docker.

The project uses a **multi-service architecture** managed with Docker Compose.

Services include:

* Django application
* PostgreSQL database
* Nginx reverse proxy

Docker ensures the application runs consistently across different environments.



## Continuous Integration (CI)

CI is implemented using **GitHub Actions**.

The pipeline automatically runs whenever code is pushed to the repository.

Pipeline steps:

1. Install project dependencies
2. Run code quality checks (flake8)
3. Run Django system checks
4. Execute unit tests
5. Build Docker image
6. Push Docker image to Docker Hub

This ensures code quality and prevents broken deployments.



## Deployment

The application is deployed using **Docker containers on Render cloud platform**.

Deployment workflow:

1. Code is pushed to GitHub
2. GitHub Actions builds Docker image
3. Image is pushed to Docker Hub
4. Render pulls the latest image and deploys the application

Live application:

https://dscc-task-manager.onrender.com



## Running the Project Locally

Follow these steps to run the project locally.

### Clone the repository

git clone https://github.com/tsoy41k/dscc-task-manager.git

### Navigate to the project directory

cd dscc-task-manager

### Install dependencies

pip install -r requirements.txt

### Apply migrations

python manage.py migrate

### Run development server

python manage.py runserver

Open the application in your browser:

http://127.0.0.1:8000



## Running with Docker

You can also run the project using Docker.

docker compose up --build

The application will be available at:

http://localhost:8000



## Environment Variables

The project uses environment variables for sensitive configuration.

Example variables:

SECRET_KEY=your_secret_key
DEBUG=False
POSTGRES_DB=dscc_db
POSTGRES_USER=dscc_user
POSTGRES_PASSWORD=dscc_password

These variables should be stored in a **.env file** and never committed to the repository.



## Testing

The project includes basic unit tests implemented using Django's testing framework.

Tests verify core application functionality including authentication and page access.

Run tests locally using:

python manage.py test



## Future Improvements

Possible improvements include:

* Task deadlines and priorities
* Task filtering and sorting
* Improved UI design
* Email verification for users
* REST API implementation



## Repository Links

GitHub Repository
https://github.com/tsoy41k/dscc-task-manager

Docker Hub Repository
https://hub.docker.com/r/tsoy41k/dscc-task-manager

Live Application
https://dscc-task-manager.onrender.com



## Test Account

Example test credentials for assessment:

Username: testuser
Password: testpass123
