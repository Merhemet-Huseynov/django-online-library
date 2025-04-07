Here's a sample `TESTS.md` file based on your provided structure:

---

## Tests 🚀🔐

This project includes a comprehensive testing suite that covers different aspects of the application. Below is an overview of the different types of tests available:

### 1. **Model Tests** 🛠️  
Model tests are used to ensure that each model behaves as expected. These tests cover things like database field validation, model methods, and relationships between models.

- **Location**: `accounts/models`, `books/models`, `reviews/models`, and similar directories for other modules.
- **Examples of Tests**:
  - Verifying that model fields are properly validated (e.g., email format, password strength).
  - Checking model relationships (e.g., one-to-many, many-to-many).
  - Ensuring that model methods function correctly (e.g., generating a slug from a book title).
  - Validating that the database schema is aligned with the models.

### 2. **API Tests** 💻  
API tests ensure that the endpoints are working as expected and that they correctly handle different types of requests (GET, POST, PUT, DELETE).

- **Location**: `accounts/tests/api`, `books/tests/api`, `reviews/tests/api`, etc.
- **Examples of Tests**:
  - Verifying that a `POST /register/` endpoint successfully creates a new user when valid data is provided.
  - Ensuring that the `GET /books/{id}/` endpoint returns the correct book details.
  - Validating authentication-related endpoints, such as `/token/` and `/token/refresh/`, to ensure they return appropriate tokens.
  - Testing error handling, like verifying that a `400` status code is returned for missing required fields or invalid input.

### 3. **View Tests** 🖥️  
View tests focus on ensuring that views (or controllers in other frameworks) are functioning correctly. These tests check that views return the expected HTTP response and render the correct templates when applicable.

- **Location**: `accounts/tests/views`, `books/tests/views`, etc.
- **Examples of Tests**:
  - Ensuring that the `GET /login/` view renders the correct template.
  - Verifying that the `POST /books/{id}/reviews/` view processes a review submission correctly.
  - Testing redirection behaviors, such as verifying that a user is redirected to a login page if they are not authenticated.

### 4. **Form Tests** 📝  
Form tests ensure that forms are correctly handling user input and displaying appropriate error messages when validation fails.

- **Location**: `accounts/forms`, `books/forms`, `reviews/forms`, etc.
- **Examples of Tests**:
  - Verifying that the registration form requires all necessary fields (email, password, etc.).
  - Ensuring that the password change form correctly validates the old and new passwords.
  - Testing the behavior of forms when invalid or missing data is provided (e.g., invalid email format).

### 5. **Authentication Tests** 🔒  
Authentication tests verify that the login, registration, password reset, and token handling processes are functioning correctly.

- **Location**: `accounts/tests/authentication`
- **Examples of Tests**:
  - Ensuring that the `POST /token/` endpoint generates an access token for valid login credentials.
  - Testing the `POST /token/refresh/` endpoint to ensure the refresh token is valid.
  - Verifying that the `POST /v1/accounts/reset-password-send-code/` endpoint sends a reset code when valid email is provided.

### 6. **Integration Tests** 🔗  
Integration tests verify that different components of the application work together as expected. These tests simulate real-world use cases where multiple features interact.

- **Location**: `integration_tests`
- **Examples of Tests**:
  - Testing the full user registration flow, from sending a verification code to completing the registration.
  - Verifying that a book purchase and rental flow is correctly processed from start to finish.

### 7. **Unit Tests** 🧪  
Unit tests focus on testing individual components or functions in isolation, ensuring that each part behaves correctly.

- **Location**: `accounts/tests/unit`, `books/tests/unit`, etc.
- **Examples of Tests**:
  - Testing utility functions (e.g., generating a slug or formatting dates).
  - Verifying that a model method like `get_full_name()` or `get_author_name()` returns the expected result.
  - Mocking external services like email or payment gateways to test the application logic without actually sending emails or processing payments.

### 8. **Performance Tests** ⚡  
Performance tests evaluate the application’s response time and scalability under various conditions.

- **Location**: `performance_tests`
- **Examples of Tests**:
  - Verifying that API endpoints handle large volumes of requests without significant performance degradation.
  - Testing database query performance with large datasets to ensure queries are optimized.

---

### Running Tests 🏃‍♂️

To run the tests for the project, use the following commands based on your environment:

#### 1. Running Tests Locally 💻

You can run the tests using `pytest`. If you don't have `pytest` installed, you can install it via:

```bash
pip install pytest
```

Once installed, run the tests by executing the following command:

```bash
pytest
```

This will automatically discover and execute all the test cases in your project.

#### 2. Running Tests with Docker 🐳

If you are using Docker for your development environment, follow these steps:

First, ensure that Docker is running and your containers are up by executing:

```bash
./scripts/start_docker.sh
```

Once the containers are running, ensure that the scripts in the `./scripts/` folder are executable by running:

```bash
chmod +x ./scripts/*
```

Then, you can execute the tests inside the web container:

```bash
docker-compose exec web pytest
```

This command will run all the tests inside the Docker container, ensuring that the environment mirrors production as closely as possible.

#### Test Coverage 📊

Test coverage is an important aspect of ensuring the quality of the application. The goal is to have as much of the codebase covered by tests as possible. You can check test coverage using tools like `pytest-cov` and generating a report. To use `pytest-cov`, install it by running:

```bash
pip install pytest-cov
```

Then, run the tests with coverage:

```bash
pytest --cov=your_project_folder
```

This will display a coverage report showing the percentage of code covered by tests.

#### Continuous Integration (CI) 🔄

To maintain high-quality code, it's important to integrate automated tests into a Continuous Integration (CI) pipeline. You can configure a CI tool (e.g., GitHub Actions, GitLab CI, or Jenkins) to automatically run tests whenever you push new changes to the repository. This helps catch errors early in the development process.

---

### Running Tests 🏃‍♂️  
To run the test suite, use the following command:

```bash
python manage.py test
```

Or, to run specific tests:

```bash
python manage.py test accounts.tests.api
```

