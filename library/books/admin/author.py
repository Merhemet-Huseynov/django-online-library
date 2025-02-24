from django.utils.html import format_html
from django.contrib import admin
from ..models import Author
from utils.slug import generate_unique_slug


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

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

    def image_preview(self, obj):
        """Shows image preview in admin panel."""
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 10px;" />', 
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = generate_unique_slug(obj.name, Author)
        super().save_model(request, obj, form, change)
