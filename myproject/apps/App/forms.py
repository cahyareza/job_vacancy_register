from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateForm(forms.ModelForm):

    # First name
    firstname = forms.CharField(
        label='First name', min_length=3, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        error_messages={"required": "First name field cannot be empty!"},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # Last name
    lastname = forms.CharField(
        label='Last name', min_length=3, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZA-y\s]*$',
        message="Only letters is allowed !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: capitalize'
            }
        )
    )

    # job code (Uppercase function)
    job = Uppercase(
        label='Job code',
        min_length=3, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Example: FR-22',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: uppercase',
                'data-mask': "AA-00",
            }
        )
    )

    # email (lowercase function)
    email = Lowercase(
        label='Email address', min_length=8, max_length=50,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Put a valid email address !")],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'input',
                'style': 'font-size: 13px; text-transform: lowercase',
                'autocomplete': 'off'
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
                'class': 'input',
                'style': 'font-size: 13px',
            }
        )
    )

    # Experience
    experience = forms.BooleanField(
        label='I have experience',
        required= False
    )

    # Message
    message = forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Talk a little about you',
                'class': 'textarea',
                'style': 'font-size: 13px',
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

    # File upload
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'file',
                'style': 'font-size: 13px',
            }
        )
    )

    class Meta:
        model = Candidate
        # fields = ['firstname', 'lastname', 'job', 'email', 'message', 'age', 'phone']
        exclude = ['create_at', 'situation']
        # labels = {
        #     'gender': "Your gender",
        #     'smoker': "Do you smoke?",
        # }


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
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            # Personality
            'personality' : forms.Select(
                attrs={
                    'class': 'input',
                    'style': 'font-size: 13px',
                }
            ),
            # Method 2
            # Gender
            'gender': forms.RadioSelect(
                choices=GENDER,
                attrs={
                    'class': 'control',
                    'style': 'font-size: 13px',
                }
            ),
            # Smoker
            'smoker': forms.RadioSelect(
                choices=SMOKER,
                attrs={
                    'class': 'control',
                    'style': 'font-size: 13px',
                }
            )
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control ========== !
        # 1. Input required
        # self.fields['message'].required = True

        # 2. Input Disabled
        # self.fields['experience'].disabled = True

        # 3. Input Readonly
        # self.fields['email'].widget.attrs.update({'readonly': 'readonly'})

        # 4. Select option
        self.fields["personality"].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[1:]

        # 5. Widget (inside/outside)
        # self.fields['phone'].widget.attrs.update({'style': 'font-size: 18px', 'placeholder': 'No phone'})

        # 6. Error messages
        self.fields['firstname'].error_messages.update({
            'required': "Django Mastery Channel"
        })

        # ========== ADVANCE CONTROL PANEL (multiple <Inputs>) ========== !
        # 1) Readonly
        # readonly = ['firstname', 'lastname', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # 2) Disable
        # disable = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary']
        # for dield in disable:
        #     self.fields[field].widget.attrs['disabled'] = "true"

        # 3) ERROR MESSAGES

        # 4) FONT SIZE
        # font_size = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary']
        # for field in font_size:
        #     self.fields[field].widget.attrs.update({'style': 'font-size: 18px'})

    # ================================= END SUPER FUNCTION ================================= !



    # 1) FUNCTION TO PREVENT DUPLICATE ENTRIES
    # Method 1 (loop for)
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError('Denied ! ' + email + ' is already registered.')
    #     return email

    # Method 2 (if statement w/ filter)
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Candidate.objects.filter(email = email).exists():
            raise forms.ValidationError('Denied ! ' + email + ' is already registered.')
        return email

    # 2) JOB CODE (Job code validation)
    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'FR-22' or job == 'BA-10' or job == 'FU-15':
            return job
        else:
            raise forms.ValidationError('Denied ! This code is invalid.')

    # 3) AGE (Range: 18 - 65)
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < '18' or age > '65':
            raise forms.ValidationError('Denied ! Age must be between 18 and 65.')
        return age

    # 4) PHONE (Prevent incomplete value)
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 15:
            raise forms.ValidationError('Phone field is incomplete.')
        return phone