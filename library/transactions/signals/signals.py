from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models.rental import RentalSchedule, OverdueFine


@receiver(post_save, sender=RentalSchedule)
def create_or_update_fine(sender, instance, **kwargs):
    """
    Update or create an overdue fine when a rental record is modified.

    This function ensures that whenever a RentalSchedule instance is saved, 
    the corresponding OverdueFine is created or updated accordingly.
    """
    fine_obj, created = OverdueFine.objects.get_or_create(rental=instance)
    fine_obj.calculate_fine()
