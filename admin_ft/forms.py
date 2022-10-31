from django import forms

class AdminForm(forms.Form):
    noted = forms.CharField(max_length=100)