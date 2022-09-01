from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator


# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


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

    # job code always in Uppercase
    job = Uppercase(
        label='Job code',
        min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Example: FR-22',
                'class': 'input'
            }
        )
    )

    # email always in Lowercase
    email = Lowercase(
        label='Email address', min_length=8, max_length=50,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
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


    experience = forms.BooleanField(
        label='I have experience',
        required= False
    )


    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Talk a little about you',
                'class': 'textarea'
            }
        ),
        help_text='Write here your message!'
    )

    # Method 1 (Gender)

    # GENDER = [('M', 'Male'), ('F', 'Female')]
    # gender = forms.CharField(
    #     label='Gender',
    #     widget=forms.RadioSelect(
    #         choices=GENDER
    #     )
    # )

    class Meta:
        model = Candidate
        # fields = ['firstname', 'lastname', 'job', 'email', 'message', 'age', 'phone']
        exclude = ['create_at', 'situation']


        SALARY = (
            ('', 'Salary expectation (month)'),
            ('Between ($3000 and $4000)', 'Between ($3000 and $4000)'),
            ('Between ($4000 and $5000)', 'Between ($4000 and $5000)'),
            ('Between ($5000 and $7000)', 'Between ($5000 and $7000)'),
        )

        GENDER = [('M', 'Male'), ('F', 'Female')]


        # OUTSIDE WIDGET
        widgets = {
            # Phone
            'phone': forms.TextInput(
                attrs={
                    'style': 'font-size: 13px',
                    'placeholder': 'Phone',
                    'data-mask': '(00) 00000-000',
                    'class': 'input'
                }
            ),
             # Salary
            'salary' : forms.Select(
                choices=SALARY,
                attrs={
                    'class': 'input'
                }
            ),
            # Personality
            'personality' : forms.Select(
                attrs={
                    'class': 'input'
                }
            ),
            # Method 2
            # Gender
            'gender': forms.RadioSelect(
                choices=GENDER,
                attrs={
                    'class': 'control'
                }
            ),
            # Smoker
            'smoker': forms.RadioSelect(
                choices=SMOKER,
                attrs={
                    'class': 'control'
                }
            )
        }
