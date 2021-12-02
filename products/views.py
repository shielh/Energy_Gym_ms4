from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category, Review
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products"""

    categories = Category.objects.all()
    products = Product.objects.all()

    if request.GET:
        # filter products by category
        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_names)

        # search by product name
        if'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # only show categories that have a product 
        categories = categories.filter(name__in=[p.category.name for p in products])

    # Links products to category name for heading
    category_products = {c.name: (c, []) for c in categories}
    for product in products:
        category_products[product.category.name][1].append(product)            

    context = {
        'category_products': category_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    # Add review
    reviewForm = ReviewForm()
    reviews = Review.objects.filter(product=product)

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'reviewForm': reviewForm,
        'reviews': reviews,
    }

    return render(request, template, context)


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
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            comments = form.cleaned_data['comments']
            rating = form.cleaned_data['rating']
            Review.objects.create(
                user=user,
                product=get_object_or_404(Product, pk=product_id),
                title=title,
                rating=rating,
                comments=comments)
            messages.success(request, 'Successfully added review.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. \
                    Please check the form is valid and try again.')
    else:
        form = ReviewForm()
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'product': product,
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
def delete_review(request, review_id):
    """
    Delete a review for a product
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=(review.product.id,)))
