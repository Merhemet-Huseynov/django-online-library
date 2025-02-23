from django.db import models
from django.utils.timezone import timedelta


class DailyMessageLimit(models.Model):
    limit = models.PositiveIntegerField(
        default=3
    )  
    expiration_time = models.DurationField(
        default=timedelta(minutes=3)
    )  
    reset_time = models.DurationField(
        default=timedelta(hours=24)
    )  

    def __str__(self):
        return (
            f"Daily Limit: {self.limit} "
            f"Expiration Time: {self.expiration_time} "
            f"Reset Time: {self.reset_time}"
        )
