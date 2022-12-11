from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
# Create your views here.
from .forms import QuestionForm
from .models import Question
from campaign.models import Campaign
import json
from django.views.decorators.csrf import csrf_exempt
import datetime



def show_homepage(request):
    form = QuestionForm()
    context = {
            "form":form,
            "last_question": request.session.get('last_login', 'have not submit a question yet')
        }
    return render(request,'homepage.html',context)

@login_required(login_url='/login/')
def submitquestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print()
            new_question = Question(
                user = request.user,
                question=request.POST.get('question'),
            )
            new_question.save()
            response = serializers.serialize('json',[new_question])
            request.session['last_question'] = str(datetime.datetime.now())
            return JsonResponse(response, safe=False)
    return HttpResponseBadRequest

@csrf_exempt
def flutter_submitquestion(request):
    print('--------------------------the function is called')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print('--------------------------the form is valid')
            new_question = Question(
                user = request.user,
                question=request.POST.get('question'),
            )
            new_question.save()
            return HttpResponse(status=201)
    return HttpResponseBadRequest


def getcampaignsum(request):
    if request.method == 'GET':
        data = str(Campaign.objects.count())
        return HttpResponse(data , content_type="text/plain")

@csrf_exempt
def flutter_getcampaignsum(request):
    if request.method == 'GET':
        print('---------------- campaign sum function called')
        data = []
        data.append({'count': Campaign.objects.count()}) 
        return  JsonResponse(data, safe=False)


def get_last_question(request):
    if request.method == 'GET':
        data = str(request.session.get('last_question', "haven't submit a question yet"))
        return HttpResponse(data , content_type="text/plain")

@csrf_exempt
def flutter_get_last_question(request):
    if request.method == 'GET':
        data = str(Campaign.objects.count())
        return HttpResponse(data , content_type="text/plain")


@login_required(login_url='/login/')
def show_json(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def flutter_getrecentquestions(request):
    print('----------------function called')
    count = Question.objects.count()
    data = []
    for x in range(3):
        if (count-x)>0:
            data.append({
                'username' : str(Question.objects.get(pk=(count-x)).user),
                'question': Question.objects.get(pk=(count-x)).question
            })
    return  JsonResponse(data, safe=False)



