from django.shortcuts import render

# Create your views here.

import datetime
from pydoc import describe
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from participate.models import Participants
from participate.forms import ParticipantsForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# @login_required(login_url='/ecoist/login/')
def show_page(request):
    context ={}
    context['form']= ParticipantsForm()
    return render(request, "participate.html", context)

# @login_required(login_url='/ecoist/login/')
def join_campaign(request):
    if request.method == "POST":
        nama = request.POST.get("nama_pendaftar")
        email = request.POST.get("email_pendaftar")
        phonenumber = request.POST.get("phone_number")
        help = request.POST.get("what_can_you_help_with")
        reason = request.POST.get("reason_to_participate")
        add_participants = Participants(nama_pendaftar=nama, email_pendaftar=email, phone_number=phonenumber, what_can_you_help_with=help, reason_to_participate=reason)
        add_participants.save()

        return HttpResponse(b"CREATED", status=201)
            
    return HttpResponseNotFound()

# @login_required(login_url='/ecoist/login/')
def show_json(request):
    data = Participants.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
