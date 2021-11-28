from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    ReviewForm allows users to leave a review
    """
    class Meta:
        model = Review
        fields = ('title', 'comments', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comments': 'Please write your review here',
        }
