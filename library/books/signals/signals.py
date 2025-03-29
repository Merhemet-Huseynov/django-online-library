from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from books.models.catalog import Book
from books.models.review import UserBookView, BookRecommendation

__all__ = [
    "create_book_recommendation",
    "update_recommendations_on_new_book",
]

@receiver(post_save, sender=UserBookView)
def create_book_recommendation(sender, instance, created, **kwargs):
    """
    Signal handler that triggers when a user views a book.

    This function recommends other books written by the same author to the user,
    provided they have not already viewed or been recommended those books.

    Args:
        sender (Model): The model class (`UserBookView`) that triggered the signal.
        instance (UserBookView): The instance that was saved.
        created (bool): Indicates whether this is a new instance or an update.
        **kwargs: Additional keyword arguments.

    If the `UserBookView` instance is newly created, the function:
    - Retrieves books written by the same author as the viewed book.
    - Excludes books the user has already viewed or been recommended.
    - Creates `BookRecommendation` entries for the eligible books.
    """
    if created:
        user = instance.user
        book = instance.book

        # Find books by the same author, excluding the viewed book
        similar_books = Book.objects.filter(author=book.author).exclude(id=book.id)

        with transaction.atomic():
            for similar_book in similar_books:
                already_viewed = UserBookView.objects.filter(
                    user=user, book=similar_book).exists()
                
                already_recommended = BookRecommendation.objects.filter(
                    user=user, book=similar_book).exists()

                if not already_viewed and not already_recommended:
                    BookRecommendation.objects.create(user=user, book=similar_book)

@receiver(post_save, sender=Book)
def update_recommendations_on_new_book(sender, instance, created, **kwargs):
    """
    Signal handler that triggers when a new book is added to the database.

    This function updates book recommendations for users who have previously 
    viewed books by the same author.

    Args:
        sender (Model): The model class (`Book`) that triggered the signal.
        instance (Book): The newly created book instance.
        created (bool): Indicates whether this is a new instance or an update.
        **kwargs: Additional keyword arguments.

    If a new `Book` instance is created, the function:
    - Identifies users who have previously viewed books by the same author.
    - Excludes users who have already viewed or been recommended the new book.
    - Creates `BookRecommendation` entries for the new book.
    """
    if created:
        author = instance.author

        # Find users who have already viewed books by this author
        users_who_viewed_author = UserBookView.objects.filter(
            book__author=author).values_list("user", flat=True).distinct()

        with transaction.atomic():
            for user_id in users_who_viewed_author:
                already_viewed = UserBookView.objects.filter(
                    user_id=user_id, book=instance).exists()
                
                already_recommended = BookRecommendation.objects.filter(
                    user_id=user_id, book=instance).exists()

                if not already_viewed and not already_recommended:
                    BookRecommendation.objects.create(user_id=user_id, book=instance)
