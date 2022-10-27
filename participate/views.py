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
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def show_page(request):
    context = {
    'nama': 'Adish',
    }
    return render(request, "participate.html", context)

def join_campaign(request):
    if request.method == "POST":
        nama = request.POST.get("nama_pendaftar")
        email = request.POST.get("email_pendaftar")
        phonenumber = request.POST.get("phone_number")
        add_participants = Participants(nama_pendaftar=nama, email_pendaftar=email, phone_number=phonenumber)
        add_participants.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_json(request):
    data = Participants.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
