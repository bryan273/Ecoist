from django.forms import ModelForm
from campaign.models import Campaign

class TaskForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description']