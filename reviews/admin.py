from django.contrib import admin
from .models import Review


class ReviewFormAdmin(admin.ModelAdmin):
    """
    Add review admin
    """
    list_display = (
        'title',
        'comments',
        'date_created',
        'user',
    )


admin.site.register(Review, ReviewFormAdmin)
