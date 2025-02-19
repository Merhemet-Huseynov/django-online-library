from django.contrib import admin
from django.utils.timezone import localtime, timedelta 
from accounts.models.verification import (
    VerificationCode, 
    DailyMessage,
    DailyMessageLimit
)


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "verification_code",
        "is_verified",
        "local_created_at",
        "is_expired_display",
    )
    list_filter = (
        "is_verified", 
        "created_at"
    )
    search_fields = (
        "email", 
        "verification_code"
    )
    readonly_fields = (
        "created_at",
    )
    
    actions = [
        "mark_as_verified", 
        "delete_expired_codes"
    ]

    def local_created_at(self, obj):
        return localtime(obj.created_at).strftime("%Y-%m-%d %H:%M:%S")

    local_created_at.admin_order_field = "created_at"
    local_created_at.short_description = "Local Time"

    def is_expired_display(self, obj):
        return obj.is_expired()
    
    is_expired_display.short_description = "Expired?"
    is_expired_display.boolean = True

    @admin.action(description="Mark selected codes as verified")
    def mark_as_verified(self, request, queryset):
        updated_count = queryset.update(is_verified=True)
        self.message_user(
            request, 
            f"{updated_count} verification codes marked as verified."
        )

    @admin.action(description="Delete expired verification codes")
    def delete_expired_codes(self, request, queryset):
        expired_codes = queryset.filter(
            created_at__lt=localtime() - timedelta(seconds=180)
        )
        deleted_count, _ = expired_codes.delete()
        self.message_user(
            request, 
            f"{deleted_count} expired verification codes deleted."
        )


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


@admin.register(DailyMessageLimit)
class DailyMessageLimitAdmin(admin.ModelAdmin):
    list_display = (
        "limit", 
        "get_expiration_time", 
        "get_reset_time"
    )
    list_editable = (
        "limit",
    ) 
    list_display_links = (
        "get_expiration_time", 
        "get_reset_time"
    )  
    readonly_fields = (
        "id",
    ) 
    fieldsets = (
        ("General Settings", {
            "fields": (
                "limit", 
                "expiration_time", 
                "reset_time"
            ),
            "description": "Set a daily message limit and reset time."
        }),
    )

    def get_expiration_time(self, obj):
        return self.format_duration(obj.expiration_time)
    get_expiration_time.short_description = "Code Expiration Date"

    def get_reset_time(self, obj):
        return self.format_duration(obj.reset_time)
    get_reset_time.short_description = "Limit Reset Period"

    def format_duration(self, duration):
        total_seconds = int(duration.total_seconds())
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        parts = [
            f"{days} day" if days else "",
            f"{hours} hour" if hours else "",
            f"{minutes} minute" if minutes else "",
            f"{seconds} second" if seconds else ""
        ]
        return " ".join(filter(None, parts)) or "0 second"
