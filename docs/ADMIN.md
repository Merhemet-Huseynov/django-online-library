### 🚀 Admin Panel Setup and Usage Guide 📦

1. **Docker Setup** 🐳:
   - **Build and Start Containers** 🔧:
     ```bash
     docker-compose up --build
     ```

2. **Migrate the Database** 🗄️:
   - **Create Migrations** ⚙️:
     ```bash
     docker-compose exec web python manage.py makemigrations
     ```
   - **Apply Migrations to the Database** 💾:
     ```bash
     docker-compose exec web python manage.py migrate
     ```

3. **Create Superuser (Admin)** 👑:
   - Create a superuser account:
     ```bash
     docker-compose exec web python manage.py createsuperuser
     ```
   - Enter the username, email, and password.

4. **Access Admin Panel** 🌐:
   - Open a web browser and go to the following address: `http://localhost:8000/admin/`
   - Log in using the superuser credentials created earlier.

5. **Usage** ⚡:
   - **Admin Features**: Use the admin panel to manage users, books, transactions, messages, and notifications. 📲
   - Admin can add, edit, and delete content across different modules such as books, transactions, messages, and notifications. 📝❌

---

### 📋 Admin Panel Models Overview

This document provides a brief overview of the models available in the Django admin panel and their usage.

#### **1. DailyMessageLimitAdmin** 🗓️📊  
Used for managing daily message sending limits for users. Admin can set or modify the message limits.

#### **2. DailyMessageAdmin** 💌  
Tracks and manages the daily messages sent by users. Admin can monitor how many messages each user has sent on a given day.

#### **3. EmailVerificationAdmin** 📧  
Manages email verification codes. Admin can verify and manage user email verification statuses.

#### **4. UserPreferencesAdmin** ⚙️  
Manages user-specific preferences. Admin can modify notification settings and other personalized options.

#### **5. AuthorAdmin** ✍️  
Manages book authors. Admin can add, edit, or remove authors from the system.

#### **6. BookAdmin** 📚  
Manages book details. Admin can add, edit, or delete books, including their titles, authors, and categories.

#### **7. BookReviewAdmin** 📝  
Handles user-submitted reviews for books. Admin can moderate reviews, editing or removing them if necessary.

#### **8. BookRecommendationAdmin** 📖  
Manages book recommendations. Admin can create, modify, or delete recommendations based on various criteria.

#### **9. CategoryAdmin** 📂  
Manages book categories. Admin can add or remove categories, ensuring proper categorization of books.

#### **10. EventScheduleAdmin** 📅  
Manages scheduled events related to books, authors, or other activities. Admin can create, edit, or delete event schedules.

#### **11. OverdueNotificationAdmin** ⏳  
Handles overdue notifications. Admin can send reminders to users about overdue items.

#### **12. PaymentAdmin** 💳  
Manages payment records. Admin can review, add, edit, or delete payment transactions related to book purchases or rentals.

#### **13. PurchaseHistoryAdmin** 🛍️  
Tracks purchase history for users. Admin can view and manage past transactions.

#### **14. RentalHistoryAdmin** 📅  
Manages rental history. Admin can view and edit user rental records.

#### **15. SaleTransactionAdmin** 💸  
Manages sale transactions. Admin can oversee sales records and transactions.

#### **16. RentalPriceAdmin** 💲  
Sets and manages rental prices for books. Admin can adjust rental costs based on book types and other factors.

#### **17. SalePriceAdmin** 🏷️  
Manages sale prices for books. Admin can modify the prices based on specific sale conditions.

#### **18. RentalScheduleAdmin** 📅  
Tracks and manages rental schedules. Admin can set and edit rental availability.

---

### 📌 Notes 📝:
- Ensure that environment variables (e.g., `SECRET_KEY`, `POSTGRES_*`, `JWT_*`) are properly configured in the `.env` file before running the setup. 🔒
- The admin panel allows for easy management of various system modules, and any changes made can directly affect the platform's functionality. Always double-check changes before finalizing.