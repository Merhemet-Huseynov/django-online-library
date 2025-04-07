### **🚀 Setup and Usage (Detailed)**

This guide will explain all the steps required to set up and run the **Django Online Library** project.

#### **📋 Requirements**

To run the project properly, the following software must be installed:

1. **Python 3.12.5**: Needed for Django and other Python libraries. 🐍
2. **Docker**: Used to run the project in a containerized environment. 🐳
3. **Docker Compose**: Used to manage multiple Docker containers. ⚙️
4. **PostgreSQL**: For the database. 💾
5. **Redis**: For Celery broker and result storage. 🔄
6. **Django**: For building the web application. 🌐
7. **Django Rest Framework (DRF)**: For building the API. 📡
8. **Celery**: For executing asynchronous tasks. 🧑‍💻
9. **JWT**: For user authentication. 🔑

#### **⚙️ Setup Steps**

1. **📥 Clone the Project**:
   Clone the project from GitHub:
   ```bash
   git clone https://github.com/Merhemet-Huseynov/django-online-library.git
   cd django-online-library
   ```

2. **🛠️ Create Virtual Environment (Using Pipenv or venv)**:
   Create a virtual environment and manage the environment using Pipenv. This allows independent management of all necessary libraries for the project.
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

   **If a virtual environment is already created, you can activate it using**:
   ```bash
   pipenv shell
   ```
   or

   Create a virtual environment using venv (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **📦 Install Required Libraries**:
   Install all libraries mentioned in the `Pipfile`:
   ```bash
   pipenv install
   ```
   or

   ```bash
   pip install -r requirements.txt
   ```

4. **🔧 Configure .env File**:
   Create a `.env` file and add the following parameters.

   Example contents of the `.env` file:

   ```ini
    # Django Configuration
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    DJANGO_SETTINGS_MODULE=library.settings

    # PostgreSQL Docker Configuration
    DATABASE_URL=postgresql://postgres:your-db-password@my-postgres:5432/mydatabase
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=your-db-password
    POSTGRES_PORT=5432

    # Redis
    REDIS_URL=redis://redis:6379/0
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0

    # SMTP
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    DEFAULT_FROM_EMAIL=your-email@example.com

   ```

5. **🐳 Build and Start Docker Containers**:
   To build and run the project using Docker, use the following command:
   ```bash
   docker-compose up --build
   ```

   This command will create and start all necessary containers (PostgreSQL, Redis, and Django application) using Docker Compose.

6. **🔄 Apply Migrations**:
   To apply the database structure to PostgreSQL in the Django application, run the following commands:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

7. **🛡️ Create Admin User**:
   To access the Django admin panel, create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

   Enter a username, email, and password to create the superuser.

8. **🧪 Run Tests (Optional)**:
   To run the tests for the project, use the following command:
   ```bash
   docker-compose exec web pytest
   ```

#### **🔍 Usage**

Using **Swagger UI** makes it easy to test the API endpoints:

1. **📊 Swagger UI**:
   To easily browse and test API endpoints, use Swagger UI:
   - Swagger UI address: `http://localhost:8000/swagger/`

2. **🔗 API Endpoints**:
   - **User Registration**:  
     `POST /api/auth/register/` 📝
   - **Login (JWT)**:  
     `POST /api/auth/login/` 🔑
   - **Book Listing**:  
     `GET /api/books/` 📚
   - **Book Details**:  
     `GET /api/books/{book_id}/` 📖
   - **Like a Book**:  
     `POST /api/books/{book_id}/like/` ❤️
   - **Add a Comment**:  
     `POST /api/books/{book_id}/comment/` 💬

3. **🖥️ Admin Panel**:
   To access the admin panel:  
   `http://localhost:8000/admin/` 🔑

#### **📁 Detailed Configuration Files**

1. **docker-compose.yml**:
   This file is used to manage the PostgreSQL, Redis, and Django application containers. Docker containers are launched based on this file. 🛠️

2. **Dockerfile**:
   Used to run the Django application inside a container. The `Dockerfile` describes the process of setting up and running the Django app. 🧑‍💻

3. **Dockerfile.celery**:
   A separate Dockerfile used to run the Celery worker in a container. This file contains the configuration for the Celery container. 🔄

4. **Pipfile**:
   Specifies the configuration of the Python environment using Pipenv. The `Pipfile` contains all libraries and environment parameters used in the project. 📦

5. **Pipfile.lock**:
   Preserves the versions of libraries from the `Pipfile`. This file determines exactly how the environment will be set up. 🔒

6. **requirements.txt**:
   If you prefer to use `requirements.txt` instead of Pipenv, this file lists all the Python libraries used in the project. For those working with Pipenv, `Pipfile` and `Pipfile.lock` should be used, but `requirements.txt` ensures that libraries are easily installed in a Python environment. 📝

7. **.env**:
   Contains the configuration parameters for the Django app and other services (PostgreSQL, Redis, Celery). It is crucial to modify this file accordingly. ⚙️