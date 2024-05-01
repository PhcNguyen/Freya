from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.template.loader import render_to_string
from .forms import ContactForm



def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string(
                'templates/contact.html', {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message
                }
            )
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')