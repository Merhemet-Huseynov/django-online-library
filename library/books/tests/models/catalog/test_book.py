import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from books.models import Book, Author, Category
from utils.slug import generate_unique_slug


@pytest.fixture
def author() -> Author:
    """
    Fixture to create an Author instance.
    
    Returns:
        Author: The created Author instance.
    """
    return Author.objects.create(
        name="Author Name", 
        birth_date="1990-01-01"
    )

@pytest.fixture
def category() -> Category:
    """
    Fixture to create a Category instance.
    
    Returns:
        Category: The created Category instance.
    """
    return Category.objects.create(
        name="Category Name"
    )

@pytest.fixture
def book(author: Author, category: Category) -> Book:
    """
    Fixture to create a Book instance with the provided author and category.
    
    Args:
        author (Author): The author of the book.
        category (Category): The category of the book.
    
    Returns:
        Book: The created Book instance.
    """
    return Book.objects.create(
        title="Book Title",
        author=author,
        category=category,
        published_date="2025-01-01",
        condition="new",
        book_format="physical"
    )

@pytest.mark.django_db
def test_book_creation(book: Book) -> None:
    """
    Test that the book object is created correctly.
    
    Args:
        book (Book): The book instance to be tested.
    """
    assert book.title == "Book Title"
    assert book.author.name == "Author Name"
    assert book.category.name == "Category Name"
    assert book.published_date == "2025-01-01"
    assert book.condition == "new"
    assert book.book_format == "physical"

@pytest.mark.django_db
def test_book_isbn_validation() -> None:
    """
    Test that an invalid ISBN raises a ValidationError.
    
    This test ensures that the ISBN field adheres to the expected format (10 or 13 digits).
    """
    book = Book(
        title="Invalid ISBN Book",
        isbn="12345", 
        author_id=1,
        published_date="2025-01-01",
        condition="new",
        book_format="physical"
    )
    with pytest.raises(ValidationError):
        book.clean()

@pytest.mark.django_db
def test_book_ebook_validation(book: Book) -> None:
    """
    Test that an E-book must have a digital file provided.
    
    Args:
        book (Book): The book instance to be tested.
    
    Raises:
        ValidationError: If the e-book is missing a digital file.
    """
    book.book_format = "ebook"
    book.digital_file = None 
    with pytest.raises(ValidationError):
        book.clean()

@pytest.mark.django_db
def test_book_isbn_unique(book: Book) -> None:
    """
    Test that ISBN is unique.
    
    This test ensures that two books cannot have the same ISBN.
    
    Args:
        book (Book): The base book instance to create a duplicate ISBN book for testing.
    
    Raises:
        IntegrityError: If a duplicate ISBN is attempted.
    """
    book1 = Book.objects.create(
        title="Book 1",
        isbn="1234567890",
        author=book.author,
        published_date="2025-01-01",
        condition="new",
        book_format="physical"
    )
    with pytest.raises(IntegrityError):
        Book.objects.create(
            title="Book 2",
            isbn="1234567890",  
            author=book.author,
            published_date="2025-01-01",
            condition="new",
            book_format="physical"
        )

@pytest.mark.django_db
def test_book_default_values(book: Book) -> None:
    """
    Test that default values are set correctly when creating a book.
    
    Args:
        book (Book): The book instance to be tested.
    """
    assert book.allow_rental is False
    assert book.available is True
    assert book.book_count == 1
    assert book.available_count == 1

@pytest.mark.django_db
def test_book_str_method(book: Book) -> None:
    """
    Test the string representation of the book.
    
    Args:
        book (Book): The book instance to be tested.
    
    Returns:
        str: The string representation of the book.
    """
    assert str(book) == "Book Title"
