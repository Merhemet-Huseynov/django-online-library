from django.contrib import admin
from accounts.models.verification import VerificationCode


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = (
        "email", 
        "verification_code", 
        "is_verified", 
        "created_at", 
        "is_expired_display"
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
    
    actions = ["mark_as_verified"]

    def is_expired_display(self, obj):
        return obj.is_expired()
    is_expired_display.short_description = "Expired?"
    is_expired_display.boolean = True

    @admin.action(description="Mark selected codes as verified")
    def mark_as_verified(self, request, queryset):
        queryset.update(is_verified=True)
