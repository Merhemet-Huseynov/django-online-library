from django.contrib import admin
from ..models import SaleTransaction


@admin.register(SaleTransaction)
class SaleTransactionAdmin(admin.ModelAdmin):
    """
    Provides configuration for the sale transaction model in the admin panel.

    list_display: Fields used to display sale transactions.
    list_filter: Fields used to filter sale transactions.
    search_fields: Fields used to search sale transactions.
    readonly_fields: Fields displayed as read-only and cannot be modified.
    actions: Actions to be applied to selected transactions.
    
    Methods:
        mark_as_completed: Marks selected sale transactions as "completed."
        mark_as_canceled: Marks selected sale transactions as "canceled."
        save_model: Performs additional checks before saving a sale transaction to the database.
        get_readonly_fields: Defines the fields that are read-only when editing an object.
    """

    list_display = ("user", "book", "sale_price", "sale_date", "status")
    list_filter = ("status", "sale_date", "user")
    search_fields = ("user__username", "book__title", "sale_price")
    readonly_fields = ("sale_price", "sale_date")
    actions = ["mark_as_completed", "mark_as_canceled"]

    def mark_as_completed(self, request, queryset):
        """
        Marks selected sale transactions as "completed."

        :param request: The user request for the admin panel
        :param queryset: The selected sale transactions
        """
        queryset.update(status="completed")
    mark_as_completed.short_description = "Mark selected transactions as completed"

    def mark_as_canceled(self, request, queryset):
        """
        Marks selected sale transactions as "canceled."

        :param request: The user request for the admin panel
        :param queryset: The selected sale transactions
        """
        queryset.update(status="canceled")
    mark_as_canceled.short_description = "Mark selected transactions as canceled"

    def save_model(self, request, obj, form, change):
        """
        Performs additional checks before saving a sale transaction to the database.

        :param request: The user request for the admin panel
        :param obj: The model object being edited
        :param form: The form data being submitted
        :param change: A flag indicating if the model is being changed
        """
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        """
        Defines the read-only fields when editing an object.

        :param request: The user request for the admin panel
        :param obj: The model object being edited
        :return: The read-only fields
        """
        if obj:  
            return self.readonly_fields + ("book", "user")
        return self.readonly_fields