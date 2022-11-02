from django import forms

class DonateForm(forms.Form):
    nominal = forms.IntegerField(min_value=1000)
    namaPohon = forms.CharField(max_length=255, required=True)
    jumlahPohon = forms.IntegerField(required=True, min_value=1)
    pesan = forms.CharField(widget=forms.Textarea)

# from donate.models import Donasi
# from django import forms

# class DonatekForm(forms.ModelForm):
#     class Meta:
#         model = Donasi
#         fields = ['nominal', 'namaPohon', 'jumlahPohon', 'pesan']

#         widgets = {
#             'nominal': forms.IntegerField(attrs={
#                 'name':'nominal',
#                 'id':'nominal',
#                 'min_value':'1000',
#             }),
#             'namaPohon': forms.CharField(attrs={
#                 'name':'namaPohon',
#                 'id':'namaPohon',
#                 'max_length':'255',
#                 'required':'true',
#             }),
#             'jumlahPohon': forms.IntegerField(attrs={
#                 'name':'jumlahPohon',
#                 'id':'jumlahPohon',
#                 'min_value':'1',
#                 'required':'true',
#             }),
#             'pesan': forms.Textarea(attrs={
#                 'name':'pesan',
#                 'id':'pesan',
#             }),
#         }