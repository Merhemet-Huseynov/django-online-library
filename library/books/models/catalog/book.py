from django.db import models
from .author import Author
from .category import Category


class Book(models.Model):
    author = models.ForeignKey(
        "Author", 
        on_delete=models.CASCADE, 
        related_name="books"
    )
    category = models.ForeignKey(
        "Category", 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="books"
    )

    title = models.CharField(
        max_length=255
    )
    isbn = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        unique=True
    )
    available = models.BooleanField(
        default=True
    )
    allow_rental = models.BooleanField(
        default=False
    )
    book_count = models.PositiveIntegerField(
        default=1
    )
    available_count = models.PositiveIntegerField(
        default=1
    )
    published_date = models.DateField()

    def __str__(self):
        return self.title

    def average_rating(self):
        """Calculates the average rating of all reviews of the book."""
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        return 0