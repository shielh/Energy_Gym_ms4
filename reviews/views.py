from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from .models import Review
from .forms import ReviewForm


def reviews(request):
    """ A view to return the review page """
    reviews = Review.objects.order_by('-date_created')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request):
    """
    Allows logged in users to leave reviews
    """
    if request.method == 'POST':
        form = WriteReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(
                request, 'Your review has been successfully added!')
            return redirect('reviews')
        else:
            messages.error(request, 'Failed to add review. Please try again!')
    else:
        form = WriteReview()

    template = 'reviews/add_review.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    try:
        review = get_object_or_404(Review, pk=review_id)
        if review.user != request.user.userprofile:
            messages.error(
                request, "You cannot edit a review you didn't create!")
            return redirect(reverse('reviews'))
        if request.method == 'POST':
            edit_form = ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                review = edit_form.save(commit=False)
                review.user = UserProfile.objects.get(user=request.user)
                edit_form.save()
                messages.success(request, 'Successfully updated review!')
                return redirect(reverse('reviews'))
            else:
                messages.error(
                    request, 'Failed to update review. Please ensure the form is valid.')

        edit_form = ReviewForm(instance=review)
        context = {
            'form': edit_form,
            'review': review,
        }

        return render(request, 'reviews/edit_review.html', context)
    except Http404:
        messages.error(request, "Sorry, that review doesn't seem to exist")
        return redirect('reviews')


@login_required
def delete_review(request, review_id):
    """ Delete a review from the site """
    try:
        review = get_object_or_404(Review, pk=review_id)
        if request.user.userprofile == review.user:
            review.delete()
            messages.success(request, 'Review deleted!')
            return redirect(reverse('reviews'))
    except Http404:
        messages.error(request, "Sorry! That review doesn't seem to exist")
        return redirect('reviews')
