from django.contrib import admin
from django.utils.timezone import localtime, timedelta 
from ..models import DailyMessage


@admin.register(DailyMessage)
class DailyMessageAdmin(admin.ModelAdmin):
    list_display = (
        "email", 
        "local_message_sent_at"
    )
    list_filter = (
        "message_sent_at",
    )
    search_fields = (
        "email",
    )
    readonly_fields = (
        "message_sent_at",
    )

    def local_message_sent_at(self, obj):
        return localtime(obj.message_sent_at).strftime("%Y-%m-%d %H:%M:%S")

    local_message_sent_at.admin_order_field = "message_sent_at"
    local_message_sent_at.short_description = "Local Time"