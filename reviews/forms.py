from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    ReviewForm allows users to leave a review
    """
    class Meta:
        model = Review
        fields = ('title', 'comments', 'rating',)