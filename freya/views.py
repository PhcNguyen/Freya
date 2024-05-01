from typing import Any
from django.shortcuts import (
    render,
    redirect,
)
from .forms import ContactForm



def home(request) -> Any:
    return render(request, 'home.html')


def contact(request) -> Any:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return redirect('success/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request) -> Any:
    return render(request, 'success.html')