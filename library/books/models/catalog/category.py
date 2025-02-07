from django.db import models
from utils.category import CATEGORY_CHOICES

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
