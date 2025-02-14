from django.db import models
from services.slug import generate_unique_slug


class Category(models.Model):
    name = models.CharField(
        "Name", 
        max_length=255,  
        unique=True
    )
    icon = models.FileField(
        "Image", 
        upload_to="categories/%Y/%m/%d/",
        null=True,
        blank=True
    )
    order = models.IntegerField(
        "Order", 
        null=True,
        blank=True,
        default=None
    )
    is_active = models.BooleanField(
        "Is active", 
        default=True
    )
    slug = models.SlugField(
        unique=True, 
        blank=True
    )
    super_category = models.ForeignKey(
        "self",
        verbose_name="Main category",
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,  
        related_name="subcategories",
        related_query_name="subcategory"
    )

    class Meta:
        unique_together = ("super_category", "order")
        ordering = ["order"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """The slug is set and the order value is automatically determined."""
        if not self.slug:
            self.slug = generate_unique_slug(self.name, Category)
        
        if self.order is None:
            self.order = self.get_next_order()
        
        super().save(*args, **kwargs)

    def get_next_order(self):
        """Returns the next order value for the super category"""
        
        last_order = Category.objects.filter(
            super_category=self.super_category
        ).aggregate(models.Max("order"))["order__max"]

        return (last_order or 0) + 1

    def get_super_category_name(self) -> str | None:
        if self.super_category is not None:
            return self.super_category.name
        return None

    @property
    def is_subcategory(self) -> bool:
        return self.super_category is not None
