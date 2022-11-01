from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(max_length=100)
    noted = forms.CharField(max_length=100)