from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    templates = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JuNRsIN2hzrbz3FGUp72CKseJWbFuag8dkDd6tELFksAE7nFEtXxCDm2a1aRHqGwvSA8B9SXA6AraMc9MaU7jBW008vKAWtmA',
        'client_secret': 'test client secret',
    }

    return render(request, templates, context)
