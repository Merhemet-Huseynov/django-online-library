### Models

1. **UserPreferences** 🛠️📱  
**Description:** This model stores user-specific preferences and settings, such as language preferences, notification settings, and display options.  
**Usage:** Users can modify their account settings by updating this model. Preferences are linked to the user account and can be accessed when customizing the user experience.

2. **VerificationCode** 🛡️📧  
**Description:** This model stores the email verification code, including the email address, verification code, and expiration time. It also manages code status (valid or expired).  
**Usage:** Used during user registration or password reset to verify the user's email address. The code is valid for 3 minutes, after which it expires.

3. **DailyMessageLimit** ⏳📊  
**Description:** Defines the daily message sending limits for users, such as the maximum number of messages allowed and the reset time.  
**Usage:** Configures the number of messages a user can send daily and the reset schedule. Helps prevent spam and excessive messaging.

4. **DailyMessage** 📩⏰  
**Description:** Represents the daily messages sent by users and tracks the limits and expiration of each message.  
**Usage:** Each message sent is recorded in this model, and the system ensures that users stay within their daily limits. Also tracks message expiration.

5. **OverdueNotification** ⏰📱  
**Description:** This model is used to notify users about overdue books or items. It includes notification content and time settings.  
**Usage:** When a book or item becomes overdue, a notification is sent to the user. The notification includes information about the overdue item and the due date.

6. **Catalog** 📚🔖  
**Description:** Represents the collection of books and items in the library catalog, categorized by author, genre, and other attributes.  
**Usage:** Books are added to this catalog, which is categorized by various factors like author, genre, or type. Users can search for and view books from this catalog.

7. **Book** 📖📚  
**Description:** Represents an individual book in the library, including its title, author, publication date, and other related metadata.  
**Usage:** Users can view and interact with books in the catalog, such as borrowing or purchasing.

8. **Category** 📚🔖  
**Description:** Defines the different categories that books belong to, such as fiction, non-fiction, history, or science.  
**Usage:** Each book is assigned a category, allowing users to filter and search books based on categories.

9. **BookReview** 🌟📝  
**Description:** Represents a review written by a user for a specific book. Includes ratings, review text, and associated metadata.  
**Usage:** Users can submit reviews for books they have read. Reviews are displayed alongside the book in the catalog.

10. **BookRecommendation** 🤖📚  
**Description:** This model generates book recommendations based on user preferences, reading history, and ratings.  
**Usage:** Recommendations are shown to users based on their past interactions, helping them discover new books aligned with their interests.

11. **RentalHistory** ⏳📖  
**Description:** This model tracks the rental history of users, including the borrowed items, rental duration, and return status.  
**Usage:** Users can view their rental history, including information about borrowed books and return due dates.

12. **PurchaseHistory** 💳📚  
**Description:** Stores the purchase history of users, including the items purchased, date of purchase, and payment details.  
**Usage:** Users can track their purchases, view receipts, and check past transactions related to book buying.

13. **RentalPrice** 💰📚  
**Description:** Represents the rental price of books or items, including the base price and any discounts or promotions.  
**Usage:** Defines how much users pay for renting books or items, considering various price configurations.

14. **RentalSchedule** 🗓️📖  
**Description:** Manages the rental schedules, including the available dates and times for book rentals.  
**Usage:** The rental schedule allows users to book books for specific time frames. It ensures that rented items are not double-booked.

15. **OverdueFine** 💸📚  
**Description:** Defines fines applied when books or items are returned past the due date. Includes fine amount and reason for the fine.  
**Usage:** When a user returns an item late, the system applies an overdue fine, which is stored in this model.

16. **SaleTransaction** 💳💵  
**Description:** This model tracks transactions related to book sales, including payment information, book details, and transaction date.  
**Usage:** When a user purchases a book, a sale transaction is recorded, allowing the system to track sales and process payments.

17. **SalePrice** 💲📚  
**Description:** Defines the price of books for sale, including discounts and promotions.  
**Usage:** The sale price model determines the price at which books are sold, considering any active discounts or sales.

18. **EventSchedule** 📅🎉  
**Description:** Represents the schedule for library events, including event name, date, time, and venue.  
**Usage:** Users can view upcoming events organized by the library, such as author talks, book launches, or reading sessions.