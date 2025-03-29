from django.db import models
from django.contrib.auth.models import User
from books.models.catalog import Book


class UserBookView(models.Model):
    """
    This model tracks the books that a user has viewed, along with 
    the date and time of the view.

    Fields:
    - `user`: A foreign key to the `User` model, indicating which 
      user viewed the book.
    - `book`: A foreign key to the `Book` model, representing the book 
      that was viewed.
    - `viewed_on`: A DateTime field that automatically records the timestamp 
      of when the book was viewed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the `UserBookView` instance.

        Returns a string showing the user, the book title, and the view timestamp.
        """
        return f"{self.user.username} viewed {self.book.title} on {self.viewed_on}"
