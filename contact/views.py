from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from profiles.models import UserProfile


def contact_form(request):
    template = 'contact/contact.html'
    user = get_object_or_404(UserProfile, user=request.user)

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
