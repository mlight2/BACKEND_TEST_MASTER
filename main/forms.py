from django import forms
# from django_select2.forms import ModelSelect2Widget
from .models import Employee

class AddEmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)

