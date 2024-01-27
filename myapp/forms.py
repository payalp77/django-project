from django import forms
from .models import Membernew

class Memberform(forms.ModelForm):
    class Meta:
        model = Membernew
        fields = ['firstname','lastname','image', 'rollno','phoneno']
  