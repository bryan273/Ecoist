from django.shortcuts import render
from campaign.models import Campaign
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from campaign.forms import TaskForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from campaign.forms import TaskForm

def show_campaign(request):
    data = Campaign.objects.all()
    context ={

        'campaigns': data,
        'form' : TaskForm,
    }
    return render(request, "campaign.html", context)

@login_required(login_url='/ecoist/login/')
@csrf_exempt
def create_campaign_with_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        campaign = Campaign.objects.create(
            user=request.user,
            title=title,
            description=description,
        )
    return HttpResponse("Success")

@login_required(login_url='/ecoist/login/')
@csrf_exempt
def delete_campaign(request, key):
    campaign = Campaign.objects.get(pk = key)
    campaign.delete()
    return HttpResponse("Success")

def show_json(request):
    data = Campaign.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")