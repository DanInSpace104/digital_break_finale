from django import forms
from .models import Claim


class CreateClaim(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['']
