from django.db import models
from django.contrib.auth.models import User
from books.models.catalog.book import Book


class BookReview(models.Model):
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name="reviews"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="book_reviews"
    )

    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    ) 
    review = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title} - Rating: {self.rating}"
