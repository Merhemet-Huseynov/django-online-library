from django.core.exceptions import ValidationError
from django.db import models


class EventSchedule(models.Model):
    """
    Represents an event schedule with details like name, location, description, start and end time, and media files.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(
        upload_to="event_images/", 
        blank=True, 
        null=True
    )
    video = models.FileField(
        upload_to="event_videos/", 
        blank=True, 
        null=True
    )

    def clean(self):
        """
        Validates that the end time is not earlier than the start time.
        """
        if self.end_time and self.start_time and self.end_time < self.start_time:
            raise ValidationError("End time cannot be earlier than start time.")

    def save(self, *args, **kwargs):
        """
        Calls full_clean() to validate the model before saving.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns the event name as a string representation.
        """
        return self.name