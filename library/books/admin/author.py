from django.utils.html import format_html
from django.contrib import admin
from ..models import Author
from utils.slug import generate_unique_slug


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Author objects.
    """

    list_display = (
        "name", 
        "bio", 
        "birth_date", 
        "slug",
        "image_preview"
    )  
    search_fields = (
        "name", 
        "bio"
    )
    list_filter = (
        "birth_date",
    ) 
    ordering = (
        "name",
    )
    readonly_fields = (
        "slug",
        "image_preview", 
    )

    fieldsets = (
        (None, {
            "fields": ("name", "bio", "birth_date", "image")
        }),
        ("Slug Information", {
            "fields": ("slug",),
        }),
        ("Image Preview", {
            "fields": ("image_preview",),
        }),
    )

    def image_preview(self, obj: Author) -> str:
        """
        Displays a preview of the author"s image in the admin panel.

        Args:
            obj (Author): The Author instance.

        Returns:
            str: HTML string with image or a message if no image exists.
        """
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 10px;" />', 
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"

    def save_model(self, request, obj: Author, form, change: bool) -> None:
        """
        Saves the Author model, generating a slug if necessary.

        Args:
            request: The current HTTP request object.
            obj (Author): The Author instance to be saved.
            form: The form being used to save the model.
            change (bool): Whether the model is being changed or created.

        Returns:
            None
        """
        if not obj.slug:
            obj.slug = generate_unique_slug(obj.name, Author)
        super().save_model(request, obj, form, change)
