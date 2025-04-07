### Project Overview

#### Library Management System 📚🏛️

This project is a robust **Library Management System** designed to facilitate a seamless and efficient experience for users, librarians, and administrators. The system provides features for book management, user authentication, rentals, purchases, and event scheduling, all integrated with real-time notifications and automated messages.

#### Key Features ✨

1. **User Authentication & Profiles**  
   - Users can register and authenticate via email.
   - Custom profiles with profile pictures, bios, and preferences.
   - Users can follow others and engage in social interactions.

2. **Book Catalog** 📚  
   - Organizes books into categories like fiction, non-fiction, and more.
   - Search and filter books by author, category, or title.
   - Ability to view detailed information about each book.

3. **Book Rental & Purchase** 🛒  
   - Users can rent or purchase books.
   - Rental history and purchase history tracking.
   - Overdue fines for late returns.

4. **Book Reviews & Recommendations** 📝  
   - Users can write and read reviews for books.
   - Personalized book recommendations based on reading history and preferences.

5. **Event Management** 🎉  
   - Schedule and manage library events such as book readings, author signings, and more.
   - Users can view event schedules and register for events.

6. **Notifications & Limits** 🔔  
   - Real-time notifications for overdue items, new books, and upcoming events.
   - Daily message limits for system messages to prevent spamming.

7. **Admin Features** 🔧  
   - Admin panel to manage books, users, rentals, and transactions.
   - Event scheduling and notifications for upcoming events.

#### Technologies Used 🛠️

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Caching:** Redis (for real-time notifications)
- **Celery:** For task scheduling and background jobs
- **Authentication:** JWT Tokens
- **Email:** SMTP for verification and notifications
- **Payments:** Integrated payment system for purchases
- **Docker:** For containerized deployment
- **Celery & Redis:** For handling background tasks like notifications and message limits

#### Models Overview 📊

The project includes a variety of models to handle different parts of the system:

- **User:** Custom user model with profiles, preferences, and follow/unfollow functionality.
- **Book:** Includes fields for title, author, category, and detailed metadata.
- **Review:** Users can submit reviews and ratings for books.
- **Rental:** Manages rental transactions, including overdue fines and rental history.
- **Sale:** Manages book sales, including pricing and transaction history.
- **Event:** Manages events held by the library, such as book signings or author events.

#### Goals 🎯

- Provide a user-friendly platform for book rentals and purchases.
- Implement a notification system to keep users informed.
- Offer a personalized experience through book recommendations and reviews.
- Ensure the system scales effectively with the addition of new books, users, and events.
- Provide administrators with an intuitive interface for managing the library's content.

#### Conclusion 🏁

This Library Management System is designed to simplify library operations, enhance user engagement, and provide a comprehensive set of features to manage books, users, and events. With a focus on ease of use, flexibility, and scalability, this project aims to improve the overall experience for both users and administrators.