from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from profiles.models import UserProfile


def contact_form(request):
    template = 'contact/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Your request has been sent!')
            return redirect(reverse('home'))
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
