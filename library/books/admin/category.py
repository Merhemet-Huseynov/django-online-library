from django.contrib import admin
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "super_category",
        "order", 
        "is_active"
    )
    list_filter = (
        "is_active", 
        "super_category"
    )
    search_fields = (
        "name",
    )
    ordering = (
        "super_category", 
        "order"
    )
    prepopulated_fields = {
        "slug": ("name",)
    }
    actions = [
        "activate_categories", 
        "deactivate_categories"
    ]

    def get_super_category_name(self, obj):
        return obj.get_super_category_name() or "No Super Category"
    get_super_category_name.short_description = "Super Category"

    def activate_categories(self, request, queryset):
        queryset.update(is_active=True)
    activate_categories.short_description = "Activate selected categories"

    def deactivate_categories(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_categories.short_description = "Deactivate selected categories"

    def get_order_display(self, obj):
        return obj.order if obj.order is not None else "Not assigned"
    get_order_display.short_description = "Order"

    def save_model(self, request, obj, form, change):
        if obj.order is None:  
            obj.order = obj.get_next_order()
        super().save_model(request, obj, form, change)
