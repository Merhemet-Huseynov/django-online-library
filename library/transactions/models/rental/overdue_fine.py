from django.db import models
from django.utils.timezone import now
from .rental_schedule import RentalSchedule


class OverdueFine(models.Model):
    rental = models.OneToOneField(
        RentalSchedule, 
        on_delete=models.CASCADE, 
        related_name="overdue_fine"
    )
    overdue_days = models.PositiveIntegerField(default=0)
    fine_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        """
        Save the overdue fine after calculating the penalty amount.
        The fine is only calculated once when the object is first created.
        """
        if not self.pk:
            self.calculate_fine()
        super().save(*args, **kwargs)
    
    def __str__(self):
        """
        Return a string representation of the overdue fine,
        including the fine amount, book title, and overdue days.
        """
        return (
            f"Overdue Fine: {self.fine_amount} AZN\n"
            f"Book: {self.rental.book.title}\n"
            f"Overdue Days: {self.overdue_days}"
        )

    def calculate_fine(self):
        """
        Calculate the number of overdue days and determine the fine amount.
        Each overdue day results in a fine of 1 AZN.
        """
        today = now().date()
        self.overdue_days = max((today - self.rental.rental_end_date).days, 0)
        self.fine_amount = self.overdue_days * 1 if self.overdue_days > 0 else 0

    def return_book(self):
        """
        Mark the book as returned, update its availability,
        and recalculate the overdue fine.
        """
        if self.rental.returned:
            raise ValueError("The book has already been returned.")

        self.rental.returned = True
        self.rental.book.available_count += 1
        self.rental.book.save()
        self.rental.save()

        self.calculate_fine()
        super().save()