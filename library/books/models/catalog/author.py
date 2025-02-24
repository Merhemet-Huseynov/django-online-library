from django.db import models
from utils.slug import generate_unique_slug


class Author(models.Model):
    """
    The Author model represents an author with their name, biography,
    birth date, image, and unique slug for URL generation.

    Attributes:
        name (str): The name of the author.
        bio (str): A short biography of the author.
        birth_date (date): The birth date of the author.
        image (Image): The author"s image.
        slug (str): A unique slug generated based on the author"s name.
    """
    
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
    image = models.ImageField(
        upload_to="authors/%Y/%m/%d/", 
        blank=True, 
        null=True
    )
    slug = models.SlugField(
        unique=True, 
        blank=True
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the Author model.

        Returns:
            str: The name of the author.
        """
        return self.name

    def save(self, *args, **kwargs) -> None:
        """
        Sets the slug before saving the object.

        If the slug is not provided, it generates a unique slug based on 
        the author"s name.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.slug:
            self.slug = generate_unique_slug(self.name, Author)
        super().save(*args, **kwargs)