from unittest.util import _MAX_LENGTH
from django import forms

NGO_CHOICES = (
('one', 'Delivering flyers'),
('two', 'Delivering flyers'),
('three', 'Delivering flyers'),)
 
# creating a form
class ParticipantsForm(forms.Form):
    nama_pendaftar = forms.CharField(max_length=50, required=True, label="Full Name")
    email_pendaftar = forms.CharField(max_length=50, required=True, label="E-mail")
    phone_number = forms.CharField(max_length=12, required=True, label="Phone Number")
    what_can_you_help_with = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                      choices=NGO_CHOICES, required=True, label="What can you help with?")
    reason_to_participate = forms.CharField(max_length=2000, widget=forms.Textarea, label="Why do you want to join us?")
