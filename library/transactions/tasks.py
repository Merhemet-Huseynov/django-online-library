from celery import shared_task
from django.utils.timezone import now
from transactions.models.rental import OverdueFine, RentalSchedule

@shared_task
def calculate_all_fines():
    """
    Update overdue fines for all active rentals.

    This task iterates through all active rentals that have not been returned,
    retrieves or creates an associated OverdueFine object, and updates the fine amount.
    """
    today = now().date()
    
    for rental in RentalSchedule.objects.filter(returned=False):
        fine_obj, created = OverdueFine.objects.get_or_create(rental=rental)
        fine_obj.calculate_fine()
