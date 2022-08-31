from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ['firstname', 'lastname', 'email', 'message']