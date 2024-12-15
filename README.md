# TodoList-RESTAPI

A simple REST API for managing a to-do list built using Django and Django REST framework.  This project allows users to create, read, update, and delete to-do items.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Contributing Guidelines](#contributing-guidelines)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)


## Project Overview

This project provides a basic RESTful API for managing a to-do list.  Users can interact with the API to create new tasks, mark tasks as complete, update task details, and delete tasks.  The API is built using Django and Django REST framework, making it easy to extend and integrate with other applications.  The core functionality revolves around a single `Task` model.

## Prerequisites

* Python 3.7+
* pip
* PostgreSQL (or another database supported by Django)


## Installation Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/harshkasat/TodoList-RESTAPI.git
   cd TodoList-RESTAPI
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate the database:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Configuration

The project uses a `settings.py` file for configuration.  You'll need to configure your database settings within this file to match your environment.  The default settings assume a PostgreSQL database.  Adjust `DATABASES` accordingly if you are using a different database.


## Usage Examples

The API provides the following endpoints:

* **GET /api/tasks/**: Retrieves a list of all tasks.
* **POST /api/tasks/**: Creates a new task.  Requires a JSON payload with `title` (string) and optionally `complete` (boolean).
* **GET /api/tasks/{id}/**: Retrieves a single task by ID.
* **PUT /api/tasks/{id}/**: Updates a task by ID.  Requires a JSON payload with `title` and/or `complete`.
* **DELETE /api/tasks/{id}/**: Deletes a task by ID.

**Example using curl to create a new task:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Buy groceries", "complete": false}' http://127.0.0.1:8000/api/tasks/
```


## API Reference

The API uses standard RESTful conventions.  The `Task` model has the following fields:

* `title` (CharField): The title of the task.
* `complete` (BooleanField): Indicates whether the task is complete (default: False).

The response format is JSON.  Error responses will include a descriptive error message.


## Contributing Guidelines

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your branch to your forked repository.
5. Create a pull request.


## Testing

The project includes basic tests using the Django testing framework.  To run the tests:

```bash
python manage.py test
```


## Deployment

Deployment instructions will depend on your chosen environment.  Consider using Docker for a consistent and portable deployment.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

This project was inspired by... (Add any inspirations or references here).



## Contact and Support

For questions or issues, please open an issue on this GitHub repository.
