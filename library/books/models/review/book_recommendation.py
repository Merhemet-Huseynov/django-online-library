from django.db import models
from django.contrib.auth.models import User
from books.models.catalog import Book
from books.models.review.book_view import UserBookView


class BookRecommendation(models.Model):
    """
    This model represents book recommendations for a user based 
    on their browsing history.

    Fields:
    - `user`: A foreign key to the `User` model, indicating 
      the user who will receive the recommendation.
    - `book`: A foreign key to the `Book` model, representing 
    the recommended book.
    - `recommended_on`: The date when the recommendation was made 
      (automatically set to the current date when the recommendation is created).
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="recommendations"
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="recommendations"
    )
    recommended_on = models.DateField(
        auto_now_add=True
    )

    def recommend_books(self):
        """
        Recommends books to the user based on the books they have viewed.
        It looks at books that are authored by the same authors as the books the user has viewed,
        excluding the books they have already viewed.

        It then creates `BookRecommendation` instances for the recommended books.
        """
        # Fetch the books the user has viewed
        viewed_books = UserBookView.objects.filter(user=self.user)
        recommended_books = []

        # Find books by the same authors as the viewed books
        for viewed in viewed_books:
            similar_books = Book.objects.filter(author=viewed.book.author).exclude(id=viewed.book.id)
            recommended_books.extend(similar_books)

        # Add the recommended books to the `BookRecommendation` model
        for book in recommended_books:
            BookRecommendation.objects.create(user=self.user, book=book)

    def __str__(self):
        """
        String representation of the recommendation.
        """
        return f"Recommendation for {self.user.username} - {self.book.title}"
