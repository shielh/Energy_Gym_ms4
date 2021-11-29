from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category, Review
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all()
    query = None
    categories = list(Category.objects.all())

    category_products = {c.name: (c, []) for c in categories}
    for product in products:
        category_products[product.category.name][1].append(product)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': list(products),
        'search_term': query,
        'current_categories': categories,
        'cps': category_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviewForm = ReviewForm()
    reviews = Review.objects.all
    
    context = {
        'product': product,
        'reviewForm': reviewForm,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but only the site owners can do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the'
                           + ' form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but only the site owners can do this')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure' +
                           ' the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but only the site owners can do this')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

def add_review_to_product(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = UserProfile.objects.get(user=request.user)
            review.product = Product.objects.get(pk=product_id)
            form.save()
            messages.success(
                request, 'Your review has been successfully added!')
            return redirect('product_detail')
        else:
            messages.error(request, 'Failed to add review. Please try again!')
    else:
        form = ReviewForm()

    template = 'products/product_detail.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def reviews(request):
    """ A view to return the review page """
    reviews = Review.objects.order_by('-date_created')
    context = {
        'reviews': reviews
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request):
    """
    Allows logged in users to leave reviews
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
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
        form = ReviewForm()

    template = 'products/product_detail.html'
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
                    request, 'Failed to update review. Please ensure the form '
                    + 'is valid.')

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
