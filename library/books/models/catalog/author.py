from django.db import models
from utils.slug import generate_unique_slug


class Author(models.Model):
    name = models.CharField(
        max_length=255
    )
    bio = models.TextField(
        blank=True, 
        null=True
    )
    birth_date = models.DateField(
        blank=True, 
        null=True
    )
    slug = models.SlugField(
        unique=True, 
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Sets the slug before saving the object."""
        if not self.slug:
            self.slug = generate_unique_slug(self.name, Author)
        super().save(*args, **kwargs)