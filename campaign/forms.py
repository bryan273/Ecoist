from django.forms import ModelForm
from campaign.models import Campaign
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={


                'name':"title",
                'id':"modal-title",
                'class':"form-control",
                'placeholder':"Title"
            }),
            'description': forms.Textarea(attrs={


                'name':"description",
                'id':"modal-description",
                'class':"form-control",
                'placeholder':"Deskripsi"
            }),
        }