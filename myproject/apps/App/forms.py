from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

class CandidateForm(forms.ModelForm):

    # VALIDATIONS
    firstname = forms.CharField(
        label='First name', min_length=3, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name',
                'class': 'input'
            }
        )
    )

    lastname = forms.CharField(
        label='Last name', min_length=3, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'class': 'input'
            }
        )
    )

    email = forms.CharField(
        label='Email address', min_length=8, max_length=50,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',
        message="Put a valid email address !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'input'
            }
        )
    )

    # Method 1

    # age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))

    # Method 2

    age = forms.CharField(
        label='Your age', min_length=2, max_length=2,
        validators= [RegexValidator(r'^[0-9]*$',
        message="Only numbers is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Age',
                'class': 'input'
            }
        )
    )

    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Talk a little about you',
                'class': 'input'
            }
        ),
        help_text='Write here your message!'
    )


    class Meta:
        model = Candidate
        fields = ['firstname', 'lastname', 'email', 'message', 'age']
        # widgets = {
        #     'lastname': forms.TextInput(attrs={'class': 'input'}),
        #     'email': forms.TextInput(attrs={'class': 'input'}),
        # }