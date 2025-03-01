from django.db import models
from django.contrib.auth.models import User


class UserPreferences(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="preferences"
    )
    favorite_categories = models.ManyToManyField(
        "Category", 
        related_name="preferred_by", 
        blank=True
    )
    favorite_authors = models.ManyToManyField(
        "Author", 
        related_name="preferred_by", 
        blank=True
    )

    def __str__(self):
        return f"Preferences for {self.user.username}"