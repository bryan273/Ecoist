from django.forms import ModelForm
from homepage.models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({
            'placeholder': 'Enter your question here',
            'cols' : '35',
        })