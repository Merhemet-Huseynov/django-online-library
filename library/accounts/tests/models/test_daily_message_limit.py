import pytest
from django.utils import timezone
from accounts.models.verification import DailyMessageLimit


@pytest.mark.django_db
def test_daily_message_limit_creation() -> None:
    """
    Test case to ensure that a DailyMessageLimit instance is correctly created
    with the given fields and that the values are correctly set.
    """
    daily_limit = DailyMessageLimit.objects.create(
                        limit=5,
                        expiration_time=timezone.timedelta(minutes=10),
                        reset_time=timezone.timedelta(hours=12),
                    ) 

    assert daily_limit.limit == 5
    assert daily_limit.expiration_time == timezone.timedelta(minutes=10)
    assert daily_limit.reset_time == timezone.timedelta(hours=12)


@pytest.mark.django_db
def test_daily_message_limit_str_method() -> None:
    """
    Test case to ensure that the __str__ method of DailyMessageLimit returns
    the correct string representation of the instance.
    """
    daily_limit = DailyMessageLimit.objects.create(
                        limit=3,
                        expiration_time=timezone.timedelta(minutes=3),
                        reset_time=timezone.timedelta(hours=24),
                    )

    expected_str = (
        "Daily Limit: 3 Expiration Time: 0:03:00 Reset Time: 1 day, 0:00:00"
    )
    assert str(daily_limit) == expected_str