from django import forms
from models import Tune

class TuneForm(forms.ModelForm):
    class Meta:
        model = Tune