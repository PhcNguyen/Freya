from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs= {
                'class': 'input1', 
                'placeholder': 'Name'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'class': 'input1', 
                'placeholder': 'Email'
            }
        )
    )
    subject = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs= {
                'class': 'input1',
                'placeholder': 'Subject'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'class': 'input1', 
                'placeholder': 'Create a message here', 
                'cols': '30', 'rows': '4'
            }
        )
    )
