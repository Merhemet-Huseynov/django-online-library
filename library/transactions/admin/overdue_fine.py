from django.contrib import admin
from ..models import OverdueFine


@admin.register(OverdueFine)
class OverdueFineAdmin(admin.ModelAdmin):
    """
    Admin configuration for OverdueFine model.
    """
    list_display = ("rental", "overdue_days", "fine_amount")
    list_filter = ("overdue_days",)
    search_fields = ("rental__book__title", "rental__user__email")
    readonly_fields = ("overdue_days", "fine_amount") 
    fields = ("rental", "overdue_days", "fine_amount") 

    def has_change_permission(self, request, obj=None):
        """
        Allows changing the fine amount in the admin panel.
        """
        return True  

    def save_model(self, request, obj, form, change):
        """
        Applies custom logic when saving the OverdueFine model.
        """
        if not obj.rental:
            obj.rental = self.get_default_rental()
        
        if not obj.fine_amount: 
            obj.fine_amount = self.calculate_fine(obj.overdue_days)
        super().save_model(request, obj, form, change)

    def calculate_fine(self, overdue_days):
        """
        Calculates the fine amount based on the overdue days.
        """
        return overdue_days * 1.00  
