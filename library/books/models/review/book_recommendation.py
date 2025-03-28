from django.db import models
from django.contrib.auth.models import User
from books.models.catalog import Book


class BookRecommendation(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="recommendations"
    )
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE, 
        related_name="recommendations"
    )

    recommended_on = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Recommendation for {self.user.username} - {self.book.title}"
