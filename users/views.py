import os
import csv

from typing import Any
from django.shortcuts import render
from freya.settings import CONTACT_CSV_DIR

from .utils import client_ip
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
            ip_address = client_ip(request)

            # Đảm bảo thư mục tồn tại
            os.makedirs(os.path.dirname(CONTACT_CSV_DIR), exist_ok=True)

            with open(CONTACT_CSV_DIR, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [name, email, subject, message, ip_address]
                )
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form': form})