from django.contrib import admin
from ..models import Author
from utils.slug import generate_unique_slug


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "name", 
        "bio", 
        "birth_date", 
        "slug"
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
    )

    fieldsets = (
        (None, {
            "fields": ("name", "bio", "birth_date")
        }),
        ("Slug Information", {
            "fields": ("slug",),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = generate_unique_slug(obj.name, Author)
        super().save_model(request, obj, form, change)