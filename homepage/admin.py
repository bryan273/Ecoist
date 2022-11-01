from atexit import register
from django.contrib import admin

from homepage.forms import QuestionForm
from .models import Question
# Register your models here.
admin.site.register(Question)
