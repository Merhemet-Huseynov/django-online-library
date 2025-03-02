from django.db import models
from django.contrib.auth.models import User

from books.models.catalog import Category, Author

class UserPreferences(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="preferences"
    )
    favorite_categories = models.ManyToManyField(
        "books.Category",  # DÜZƏLDİLDİ
        related_name="preferred_by", 
        blank=True
    )
    favorite_authors = models.ManyToManyField(
        "books.Author",  # DÜZƏLDİLDİ
        related_name="preferred_by", 
        blank=True
    )

    def __str__(self):
        return f"Preferences for {self.user.username}"
