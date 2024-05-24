from typing import Any
from django.shortcuts import (
    render,
)
from .forms import ContactForm



def home(request) -> Any:
    return render(request, 'users/home.html')


def contact(request) -> Any:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form': form})