from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control', 
                'placeholder': 'Name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'class': 'form-control', 
                'placeholder': 'Email'
            }
        )
    )
    subject = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Subject'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'class': 'form-control', 
                'placeholder': 'Create a message here', 
                'cols': '30', 'rows': '4'
            }
        )
    )
