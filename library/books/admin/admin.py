from django.contrib import admin
from ..models import BookReview, BookRecommendation

# Register your models here.
admin.site.register(BookReview)
admin.site.register(BookRecommendation)