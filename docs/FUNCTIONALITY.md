### Functionality

#### 1. **User Authentication & Profile Management**
   - **Registration:**  
     Users can create an account by providing their email, first name, last name, date of birth, and a password. A verification code is sent to their email for confirmation before registration is completed.
   - **Login:**  
     Users authenticate via email and password, receiving a JWT token for session management.
   - **Profile:**  
     Users can view and update their profile, which includes their profile picture, bio, and preferences (e.g., preferred book categories).
   - **Follow/Unfollow:**  
     Users can follow or unfollow other users, forming a social connection within the platform.

#### 2. **Book Management**
   - **Catalog:**  
     Books are organized into categories (e.g., Fiction, Non-fiction, Science, etc.). Each book has details like title, author, publication date, and ISBN.
   - **Search & Filters:**  
     Users can search for books by title, author, category, or ISBN. Filters allow narrowing down results based on specific criteria like availability or popularity.
   - **Book Details:**  
     Clicking on a book displays its detailed information, including the author, synopsis, reviews, and rental/purchase options.

#### 3. **Book Rental & Purchase**
   - **Rent a Book:**  
     Users can rent books for a predefined period. If a book is not available, they can be placed on a waitlist.
   - **Purchase a Book:**  
     Users can buy books outright, with the option to pay securely through an integrated payment system.
   - **Rental History:**  
     Users can view their rental history, including rental dates, due dates, and any overdue fines.
   - **Overdue Fines:**  
     Fines are automatically applied if a rented book is not returned on time. The fine is calculated based on the rental price and overdue duration.

#### 4. **Book Reviews & Recommendations**
   - **Submit Reviews:**  
     Users can submit text reviews and a rating (1-5 stars) for books they’ve rented or purchased.
   - **View Reviews:**  
     Users can read reviews left by others, helping them make informed decisions about a book.
   - **Book Recommendations:**  
     Personalized book recommendations are made based on the user’s past rentals, purchases, and rated books. Recommendations are also influenced by the user’s preferred genres and authors.

#### 5. **Event Management**
   - **Event Scheduling:**  
     Administrators can schedule library events (e.g., author talks, book signings). Each event includes the date, time, location, and a description.
   - **Event Registration:**  
     Users can register for upcoming events, receiving notifications and reminders as the event approaches.
   - **Event Notifications:**  
     Users receive notifications about new events, reminders about upcoming ones, and event cancellations or updates.

#### 6. **Notifications & Alerts**
   - **Overdue Notifications:**  
     Users are notified when they have overdue items or fines, ensuring they stay updated on their account status.
   - **Event Notifications:**  
     Users are alerted about new events or changes to scheduled events they’re registered for.
   - **Daily Message Limits:**  
     The system ensures that users can only receive a limited number of system messages (such as reminders or alerts) per day to avoid spam.
   
#### 7. **Admin Features**
   - **Book Management:**  
     Admins can add, update, and remove books from the catalog. They can also manage book categories and metadata.
   - **User Management:**  
     Admins can view, edit, or delete user accounts, handle user bans, and review user activity logs.
   - **Transaction Management:**  
     Admins can track book rentals, purchases, and fine payments. They can also manage the transaction history of users.
   - **Event Management:**  
     Admins can create, update, or cancel events, monitor registrations, and communicate with attendees.
   
#### 8. **Payment Integration**
   - **Book Purchases:**  
     Users can purchase books using integrated payment gateways. The system supports multiple payment methods such as credit cards or e-wallets.
   - **Fine Payments:**  
     Users can pay any overdue fines through the payment system, ensuring their account remains in good standing.

#### 