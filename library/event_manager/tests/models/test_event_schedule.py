import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from event_manager.models.event import EventSchedule


@pytest.mark.django_db
def test_event_schedule_end_time_validation() -> None:
    """
    Ensure that a ValidationError is raised if the end time is earlier than the start time.
    """
    start_time: timezone.datetime = timezone.now()
    end_time: timezone.datetime = start_time - timezone.timedelta(hours=1)

    event: EventSchedule = EventSchedule(
        name="Test Event",
        location="Test Location",
        description="Test Description",
        start_time=start_time,
        end_time=end_time
    )

    with pytest.raises(ValidationError):
        event.clean()


@pytest.mark.django_db
def test_event_schedule_save() -> None:
    """
    Ensure that the save method calls full_clean and does not raise an error when validation passes.
    """
    start_time: timezone.datetime = timezone.now()
    end_time: timezone.datetime = start_time + timezone.timedelta(hours=1)

    event: EventSchedule = EventSchedule(
        name="Test Event",
        location="Test Location",
        description="Test Description",
        start_time=start_time,
        end_time=end_time
    )

    event.save()

    saved_event: EventSchedule = EventSchedule.objects.get(id=event.id)
    assert saved_event.name == event.name
    assert saved_event.location == event.location
    assert saved_event.start_time == event.start_time
    assert saved_event.end_time == event.end_time


@pytest.mark.django_db
def test_event_schedule_without_end_time() -> None:
    """
    Ensure that an event can be saved without specifying an end time.
    """
    start_time: timezone.datetime = timezone.now()

    event: EventSchedule = EventSchedule(
        name="Test Event",
        location="Test Location",
        description="Test Description",
        start_time=start_time,
        end_time=None
    )

    event.save()

    saved_event: EventSchedule = EventSchedule.objects.get(id=event.id)
    assert saved_event.end_time is None
