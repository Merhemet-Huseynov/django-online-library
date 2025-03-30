from django.contrib import admin
from django.utils.html import mark_safe
from ..models import EventSchedule


@admin.register(EventSchedule)
class EventScheduleAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for EventSchedule model.
    """
    list_display = (
        "name", 
        "location", 
        "start_time", 
        "end_time", 
        "image_preview", 
        "video_preview"
    )
    search_fields = (
        "name", 
        "location", 
        "description"
    )
    list_filter = (
        "start_time", 
        "end_time"
    )
    ordering = (
        "-start_time",
    )

    def image_preview(self, obj):
        """
        Returns a preview of the event image in the admin panel.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No image"

    image_preview.short_description = "Image Preview"

    def video_preview(self, obj):
        """
        Returns a link to view the event video in the admin panel.
        """
        if obj.video:
            return mark_safe(f'<a href="{obj.video.url}" target="_blank">View Video</a>')
        return "No video"

    video_preview.short_description = "Video Preview"
