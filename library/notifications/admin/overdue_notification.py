from django.contrib import admin
from ..models import OverdueNotification


@admin.register(OverdueNotification)
class OverdueNotificationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the OverdueNotification model.
    
    Customizes the display, filtering, searching, and ordering of overdue notifications.
    """
    list_display = ("user", "book", "notification_sent_date")
    list_filter = ("notification_sent_date", "user")  
    search_fields = ("user__username", "book__title")  
    ordering = ("-notification_sent_date",)
