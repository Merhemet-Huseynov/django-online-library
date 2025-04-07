### Online Library Backend

**Description:**  
Backend for an online library system built with **Django** and **Django REST Framework**. Users can manage books, borrow and return them, submit reviews, and receive personalized recommendations. Admins can manage users, books, and transactions. 📚

#### **Key Features:**
- **Book Catalog**: Browse books by category, title, or author. 📖
- **Book Rental & Purchase**: Rent or purchase books with secure transactions. 💳
- **User Profiles**: Manage profiles and track borrowed books. 👤
- **Reviews & Ratings**: Share reviews and rate books. ⭐
- **Follow Authors**: Follow authors to stay updated on their latest books. ✍️
- **Notifications**: Receive alerts for overdue books, new arrivals, and events. 🔔

#### **Registration Process:**  
Users must verify their email before completing the registration process. 📧

For a detailed overview, see the **PROJECT_OVERVIEW.md** file.

---

### Project Goals

1. **User Management:**  
   - Registration via email with email verification. 🌐
   - Profile creation, updates, and password management. 🔐
   
2. **Catalog Management:**  
   - View, search, and filter books. 📚
   - Borrow and purchase books. 💳

3. **Book Reviews & Ratings:**  
   - Submit and view reviews for books. 📝

4. **Recommendations:**  
   - Get personalized book suggestions based on your reading history. 📚

5. **Admin Management:**  
   - Admins can manage books, users, and transactions. 👨‍💼

6. **Event Management:**  
   - Admins can create and manage library events (e.g., book clubs, author talks). 📅

For more details, see **PROJECT_OVERVIEW.md**.

---

### Models

1. **CustomUser** 👤: Custom user model with email as the unique identifier.
2. **Book** 📚: Represents books in the library catalog.
3. **Rental** 💼: Tracks book rentals and purchases.
4. **Review** ⭐: Stores user-submitted reviews and ratings.
5. **Author** ✍️: Represents authors whose books are available in the catalog.
6. **Follow** 🔄: User follow relationships to track followed authors.
7. **Event** 📅: Represents library events and activities.
8. **Notification** 🔔: Stores notifications sent to users (overdue books, new arrivals, etc.).

Refer to **MODELS.md** for detailed model structure.

---

### API Endpoints

1. **User Authentication** 🔑:  
   - `/auth/login/`: User login  
   - `/auth/register/`: User registration  
   - `/auth/logout/`: User logout  
   - `/auth/verify-email/`: Email verification  

2. **Book Management** 📚:  
   - `/v1/books/`: List all books  
   - `/v1/books/{book_id}/`: View book details  
   - `/v1/books/borrow/`: Borrow a book  
   - `/v1/books/purchase/`: Purchase a book  

3. **Review & Rating** ⭐:  
   - `/v1/reviews/`: Submit a review  
   - `/v1/reviews/{book_id}/`: View reviews for a specific book  

4. **Profile Management** 👤:  
   - `/v1/profile/`: View and update user profile  
   - `/v1/profile/rentals/`: View current and past rentals  

For more API details, check **API.md**.

---

### Core Functionalities

- **User Registration & Authentication** ✉️🔒:  
  Email verification, JWT authentication.

- **Book Catalog & Transactions** 📚💳:  
  Borrow, purchase, and manage books.

- **Reviews & Ratings** ⭐📖:  
  Submit reviews and rate books.

- **Personalized Recommendations** 📚:  
  Suggest books based on user history and preferences.

- **Admin Panel** 👨‍💼:  
  Admins can manage users, books, and transactions.

For a full functionality list, refer to **FUNCTIONALITY.md**.

---

### 🛠 Technologies

- **Django** – Web framework 🚀
- **Django REST Framework** – For API development 📦
- **PostgreSQL** – Database 🗄️
- **Celery** – For executing asynchronous tasks ⏳
- **Redis** – Celery broker and result storage 🔥
- **JWT** – User authentication 🔐
- **Docker** 🐳 – Containerized environment 🚢

---

### Project Structure

- **`library_backend/`**: Core Django project with settings and configurations. 🚀
- **`users/`**: Handles user registration, login, and profiles. 👤
- **`books/`**: Manages books and related functionalities. 📚
- **`reviews/`**: Handles reviews for books. ⭐
- **`transactions/`**: Manages book rentals and purchases. 💳
- **`notifications/`**: Handles notifications for overdue books and new arrivals. 🔔
- **`events/`**: Manages library events. 📅
- **`tests/`**: Unit tests for models, views, and serializers. 🧪

For a detailed structure, refer to the **PROJECT_STRUCTURE.md** file.

---

### Admin Panel Setup

1. **Docker Setup**:  
   ```bash
   docker-compose up --build 🚀
   ```

2. **Migrate Database**:  
   ```bash
   docker-compose exec web python manage.py makemigrations 📦
   docker-compose exec web python manage.py migrate 📦
   ```

3. **Create Superuser**:  
   ```bash
   docker-compose exec web python manage.py createsuperuser 👤
   ```

4. **Access Admin**:  
   - Go to `http://localhost:8000/admin/` and log in. 🔑

---

### Notes:
- Ensure `.env` variables are set (e.g., `SECRET_KEY`, `POSTGRES_*`).

For detailed information about admin models and their usage, refer to **ADMIN.md**. 📄

For detailed test structure, see the **TESTS.md** file. 🧪

---

### Tests

This project includes the following test types:

1. **Model Tests**: Verifying model functionality (located in `users`, `books`, `reviews`, `transactions`) 🛠️.
2. **Serializer Tests**: Ensuring correct data serialization/deserialization (in the `serializers` folder) 📦.
3. **View Tests**: Validating API/web page responses (in the `views` folder) 🌐.
4. **Integration Tests**: Ensuring API endpoints and models work correctly (in `tests/models`, `tests/serializers`, and `tests/views`) 🔗.

### Running Tests

To run the tests:

- **Standard Run**:  
  ```bash
  pytest 🚀
  ```

- **With Docker**:  
  ```bash
  ./scripts/start_docker.sh 🐳
  docker-compose exec web pytest 🔥
  ```

For detailed test structure, see the **TESTS.md** file 📑.

---

### 🚀 Setup and Usage

This guide explains how to set up and run the **Online Library Backend Django DRF** project.

#### 📋 Requirements

1. **Python 3.12.5**
2. **Docker** & **Docker Compose**
3. **PostgreSQL** (Database)
4. **Redis** (Celery Broker)
5. **Django** & **Django Rest Framework (DRF)**
6. **Celery**
7. **JWT** (User Authentication)

#### ⚙️ Setup Steps

1. **📥 Clone the Project**:
   ```bash
   git clone https://github.com/yourusername/online-library-backend.git
   cd online-library-backend
   ```

2. **🛠️ Create Virtual Environment**:
   ```bash
   pip install pipenv
   pipenv install --dev
   pipenv shell
   ```

3. **📦 Install Libraries**:
   ```bash
   pipenv install
   ```

4. **🔧 Configure .env File**:
   Add necessary configurations like `SECRET_KEY`, `DATABASE_URL`, and `REDIS_URL` in the `.env` file.

5. **🐳 Build and Start Docker Containers**:
   ```bash
   docker-compose up --build
   ```

6. **🔄 Apply Migrations**:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

7. **🛡️ Create Admin User**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

8. **🧪 Run Tests (Optional)**:
   ```bash
   docker-compose exec web pytest
   ```

#### 🔍 Usage

1. **📊 Swagger UI**:
   Access the API via Swagger: `http://localhost:8000/swagger/`

2. **🔗 API Endpoints**:
   - **User Registration**: `POST /api/auth/register/`
   - **Login (JWT)**: `POST /api/auth/login/`
   - **Book Creation**: `POST /api/books/`
   - **Book Listing**: `GET /api/books/`
   - **Rent a Book**: `POST /api/books/{book_id}/rent/`
   - **Submit a Review**: `POST /api/books/{book_id}/review/`

3. **🖥️ Admin Panel**:  
   `http://localhost:8000/admin/`

#### 📁 Configuration Files

- **docker-compose.yml** – Manages containers.
- **Dockerfile** – For running the Django app.
- **Dockerfile.celery** – For running Celery worker.
- **Pipfile** & **Pipfile.lock** – Manages the Python environment.
- **requirements.txt** – Alternative to Pipfile.
- **.env** – Configuration for Django, PostgreSQL, Redis, Celery.

---

For detailed configuration, refer to **CONFIGURATION.md**.