from django.contrib import admin
from ..models import Payment
from django.contrib.admin import ModelAdmin
from typing import Type, Dict, Callable


@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    """
    Configuration for managing the Payment model in the Django admin panel.
    
    This class provides the necessary parameters for efficiently managing payments:
    - `list_display`: Defines the main fields to display for each payment.
    - `list_filter`: Enables filtering payments based on certain fields.
    - `search_fields`: Provides search functionality in the admin panel.
    - `ordering`: Specifies how payments should be ordered in the list.
    - `date_hierarchy`: Adds hierarchical grouping by date.
    - `get_actions`: Customizes available actions, allowing only `superuser` to delete payments.
    """
    
    list_display: tuple[str] = (
        "user", 
        "book", 
        "amount", 
        "status", 
        "payment_date", 
        "transaction_id"
    )
    list_filter: tuple[str] = (
        "status", 
        "payment_date"
    )
    search_fields: tuple[str] = (
        "user__username", 
        "book__title", 
        "transaction_id"
    )
    ordering: tuple[str] = (
        "-payment_date",
    )
    date_hierarchy: str = "payment_date"
    list_per_page: int = 20
    
    def get_actions(self, request) -> Dict[str, Callable]:
        """
        Defines the actions available in the admin panel. 
        Allows deletion only for `superuser`.
        
        Args:
            request: The HTTP request object.
        
        Returns:
            dict: A dictionary of available admin actions.
        """
        actions = super().get_actions(request)
        if request.user.is_superuser:
            return actions
        else:
            del actions["delete_selected"]
            return actions
