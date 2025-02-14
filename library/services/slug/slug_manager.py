from utils.slug import convert_to_slug
from django.db import models


def generate_unique_slug(base_name, model_class):
    """
    Provides a unique slug generation based on the given model class.

    :param base_name: Base name to create the slug from
    :param model_class: Model class, e.g. Author, Category, etc.
    :return: Unique slug
    """
    base_slug = convert_to_slug(base_name)
    slug = base_slug
    counter = 1

    while model_class.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
