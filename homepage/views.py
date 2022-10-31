from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
# Create your views here.
from .forms import QuestionForm
from .models import Question
from campaign.models import Campaign
import json


def show_homepage(request):
    form = QuestionForm()
    context = {
        "form":form
    }
    return render(request,'homepage.html',context)

@login_required
def submitquestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = Question(
                question=request.POST.get('question'),
            )
            new_question.save()
            response = json.loads(serializers.serialize('json',[new_question]))
            return JsonResponse(response, safe=False)
    return HttpResponseBadRequest

def getcampaignsum(request):
    if request.method == 'GET':
        data = Campaign.objects.count()
        return HttpResponse(serializers.serialize('json',data), content_type='application/json')