from .models import *
from django import forms

class ck_forms(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__" 