from django import forms

class DonateForm(forms.Form):
    nominal = forms.IntegerField(min_value=1000)
    namaPohon = forms.CharField(max_length=255, required=True)
    jumlahPohon = forms.IntegerField(required=True, min_value=0)
    pesan = forms.CharField(widget=forms.Textarea)