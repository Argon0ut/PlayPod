from django import forms
from models import Track

class TuneForm(forms.ModelForm):
    class Meta:
        model = Track