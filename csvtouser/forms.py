from django import forms
from .models import UserFile

class AddForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ('filepath',)
