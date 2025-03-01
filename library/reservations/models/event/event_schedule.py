from django.db import models


class EventSchedule(models.Model):
    name = models.CharField(
        max_length=255
    )
    location = models.CharField(
        max_length=255
    )
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name