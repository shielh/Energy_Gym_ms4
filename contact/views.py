from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_form(request):
    template = 'contact/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been sent!')
            return render(request, 'contact/contact.html')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
