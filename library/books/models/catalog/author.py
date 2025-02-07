from django.db import models
from utils.slug import custom_slugify

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
            counter = 1
            while Author.objects.filter(slug=self.slug).exists():
                self.slug = f"{custom_slugify(self.name)}-{counter}"
                counter += 1  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name