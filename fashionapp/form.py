from django import forms
from . models import Fashion

class fashionform(forms.ModelForm):
    class Meta:
        model=Fashion
        fields=['name','desc','price','img']