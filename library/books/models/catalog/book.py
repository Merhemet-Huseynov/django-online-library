from django.db import models
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError
from typing import Optional

from .author import Author
from .category import Category
from utils.slug import generate_unique_slug


class Book(models.Model):
    """Book model - stores basic book information."""

    # Main relationships
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

    # Basic information
    title = models.CharField(max_length=255)
    isbn = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True
    )
    description = models.TextField(
        blank=True, 
        null=True
    )
    published_date = models.DateField()

    # Condition and format
    CONDITION_CHOICES = [
        ("new", "New"),
        ("good", "Good"),
        ("old", "Old"),
        ("damaged", "Damaged"),
    ]
    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
        default="new"
    )

    FORMAT_CHOICES = [
        ("physical", "Physical"),
        ("ebook", "E-Book"),
        ("both", "Both"),
    ]
    book_format = models.CharField(
        max_length=10,
        choices=FORMAT_CHOICES,
        default="physical"
    )

    image = models.ImageField(
        upload_to="book_images/%Y/%m/%d/",
        blank=True,
        null=True
    )
    tags = TaggableManager(
        blank=True
    )

    # Physical book details
    page_count = models.PositiveIntegerField(
        blank=True, 
        null=True
    )
    edition = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
    )
    publisher = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    language = models.CharField(
        max_length=50, 
        default="English"
    )
    shelf_location = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
    )

    # Digital books
    digital_file = models.FileField(
        upload_to="ebooks/",
        blank=True,
        null=True
    )

    # Rental features
    allow_rental = models.BooleanField(
        default=False
    )
    available = models.BooleanField(
        default=True
    )
    book_count = models.PositiveIntegerField(
        default=1
    )
    available_count = models.PositiveIntegerField(
        default=1
    )

    # Other general fields
    added_date = models.DateTimeField(
        auto_now_add=True
    )
    slug = models.SlugField(
        unique=True, 
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the Book object, 
        which is the book's title.

        Returns:
            str: The title of the book.
        """
        return self.title
    
    
    def save(self, *args, **kwargs) -> None:
        """
        Sets the slug before saving the object.

        If the slug is not provided, it generates a unique slug based on 
        the book"s name.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.slug:
            self.slug = generate_unique_slug(self.title, Book)
        super().save(*args, **kwargs)

    def clean(self) -> None:
        """
        Validates the book's data before saving, ensuring the 
        ISBN and book format are correct.

        - Ensures the ISBN is either 10 or 13 digits long.
        - If the book is in eBook format, it checks that a digital 
        file is provided.

        Raises:
            ValidationError: If the ISBN or eBook file validation fails.
        """
        if self.isbn and (len(self.isbn) not in [10, 13] or not self.isbn.isdigit()):
            raise ValidationError("ISBN must be 10 or 13 digits.")

        if self.book_format == "ebook" and not self.digital_file:
            raise ValidationError(
                "An E-Book file must be provided for E-Book format."
            )

        super().clean()
