from django.db import transaction
from datetime import timedelta
from payments.models.payment import Payment
from transactions.models.rental import RentalSchedule
from rest_framework import serializers


class RentalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalSchedule
        fields = ["id", "user", "book", "rental_duration", "rental_price"]

    def create(self, validated_data):
        """
        Create a rental schedule, process payment, and update rental status atomically.

        This method performs the following steps:
        1. Validates if the rental price is set.
        2. Checks if the book is available for rent.
        3. Creates a rental schedule record.
        4. Processes payment for the rental.
        5. Updates book availability and rental status.

        :param validated_data: Data validated for the rental schedule.
        :return: The created rental schedule object.
        :raises serializers.ValidationError: If the book is unavailable or the rental price is not set.
        """
        user = validated_data["user"]
        book = validated_data["book"]
        rental_duration = validated_data["rental_duration"]
        rental_price = validated_data["rental_price"]

        # Check if rental_price is None and raise a ValidationError if so
        if rental_price is None:
            raise serializers.ValidationError("The rental price cannot be null.")

        # Begin a database transaction to ensure atomicity
        with transaction.atomic():
            self._check_book_availability(book)
            self._check_rental_price(rental_price)

            # Create rental schedule
            rental_schedule = self._create_rental_schedule(user, book, rental_duration, rental_price)

            # Process payment
            self._process_payment(user, book, rental_price)

            # Update book availability and rental status
            self._update_rental_status(rental_schedule, book, rental_duration)

            return rental_schedule

    def _check_book_availability(self, book):
        """
        Check if the book is available for rent.

        :param book: The book to check availability.
        :raises serializers.ValidationError: If the book is unavailable.
        """
        if book.available_count <= 0:
            raise serializers.ValidationError("The book is currently not available for rent.")

    def _check_rental_price(self, rental_price):
        """
        Ensure the rental price is set and valid.

        :param rental_price: The price for renting the book.
        :raises serializers.ValidationError: If the rental price is not set.
        """
        if not rental_price:
            raise serializers.ValidationError("The rental price for the book is not set.")

    def _create_rental_schedule(self, user, book, rental_duration, rental_price):
        """
        Create and save the rental schedule record.

        :param user: The user who rents the book.
        :param book: The book being rented.
        :param rental_duration: The duration of the rental.
        :param rental_price: The rental price for the book.
        :return: The created rental schedule object.
        """
        return RentalSchedule.objects.create(
            user=user,
            book=book,
            rental_duration=rental_duration,
            rental_price=rental_price,
            status="pending"
        )

    def _process_payment(self, user, book, rental_price):
        """
        Process the payment for the rental.

        Creates a payment record, sets the status to "completed", and saves the payment.

        :param user: The user who is making the payment.
        :param book: The book being rented.
        :param rental_price: The price for renting the book.
        """
        payment = Payment.objects.create(
            user=user,
            book=book,
            amount=rental_price,
            status=Payment.PENDING,
            payment_method=Payment.BALANCE,  
        )

        # Update payment status to completed
        payment.status = Payment.COMPLETED
        payment.save()

    def _update_rental_status(self, rental_schedule, book, rental_duration):
        """
        Update the rental schedule and book availability after payment.

        This method marks the rental as active, reduces book availability,
        and sets the rental end date based on the duration.

        :param rental_schedule: The rental schedule object to update.
        :param book: The book being rented.
        :param rental_duration: The duration of the rental.
        """
        # Mark the rental as active
        rental_schedule.status = "active"
        rental_schedule.book.available_count -= 1
        rental_schedule.book.save()

        # Calculate the rental end date based on the duration
        rental_schedule.rental_end_date = self._calculate_rental_end_date(
            rental_schedule.rental_start_date, 
            rental_duration
        )
        rental_schedule.save()

    def _calculate_rental_end_date(self, start_date, rental_duration):
        """
        Calculate the rental end date based on the rental duration.

        :param start_date: The rental start date.
        :param rental_duration: The duration of the rental.
        :return: The calculated rental end date.
        """
        if rental_duration == "3_days":
            return start_date + timedelta(days=3)
        elif rental_duration == "1_week":
            return start_date + timedelta(weeks=1)
        elif rental_duration == "1_month":
            return start_date + timedelta(weeks=4)
        return start_date
