from django.core.management.base import BaseCommand
from books.models.catalog import Category
from utils.category import CATEGORY_CHOICES

class Command(BaseCommand):
    help = "Create categories from CATEGORY_CHOICES"

    def handle(self, *args, **kwargs):
        for main_category, subcategories in CATEGORY_CHOICES.items():
            # Create the main category (with parent=None)
            category, created = Category.objects.get_or_create(name=main_category)

            # Create sub-categories
            for subcategory, subcategory_name in subcategories.items():
                Category.objects.get_or_create(name=subcategory_name, parent=category)

        self.stdout.write(self.style.SUCCESS("Categories successfully created"))