from django.db import models
from .rental_schedule import RentalSchedule

class OverdueFine(models.Model):
    rental = models.OneToOneField(
        RentalSchedule, 
        on_delete=models.CASCADE, 
        related_name="overdue_fine"
    )

    overdue_days = models.PositiveIntegerField(default=0)
    fine_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return (
            f"Overdue Fine: {self.fine_amount} AZN\n"
            f"Book: {self.rental.book.title}\n"
            f"Overdue Days: {self.overdue_days}"
        )

    def return_book(self):
        """Return the book and create a record by calculating the fine."""
        if self.returned:
            raise ValueError("The book has already been returned.")

        self.returned = True
        self.book.available_count += 1
        self.book.save()

        # Calculation of fines for overdue books
        today = now().date()
        overdue_days = max((today - self.rental_end_date).days, 0)

        fine_amount = 0
        if overdue_days > 0 or self.status == "pending":  
            fine_amount = overdue_days * 1 

            OverdueFine.objects.create(
                rental=self,
                overdue_days=overdue_days,
                fine_amount=fine_amount
            )

        self.save()