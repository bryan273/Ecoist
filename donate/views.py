from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from donate.models import Donasi
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.core import serializers
from donate.forms import DonateForm
from django. views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
# @login_required(login_url='login/')
def show_donate(request):
    context = {'form':DonateForm()}
    return render(request, "donate.html", context)

# @ensure_csrf_cookie
@csrf_exempt
def flutter_donation(request):
    if request.method == 'POST':
        print("apapun")
        print(request.POST.get('nominal'), request.POST.get('pesan'))

        # try:
            # user = User.objects.get(username = request.POST.get('nama'))
        nominal = request.POST.get("nominal")
        namaPohon = request.POST.get("namaPohon")
        jumlahPohon = request.POST.get("jumlahPohon")
        pesan = request.POST.get("pesan")
        donation = Donasi(user=request.user,nominal=nominal,namaPohon=namaPohon,jumlahPohon=jumlahPohon,pesan=pesan)
        donation.save()

        return JsonResponse({"instance":'proyek dibuat'}, status=200)
        # except:
        #     return JsonResponse({"instance":'proyek gagal'}, status=401)
    else:
        return JsonResponse({"gagal"}, status=404)

# @login_required(login_url='login/')
def donate_ajax(request):
    if request.method == 'POST':
        nominal = request.POST.get('nominal')
        namaPohon = request.POST.get('namaPohon')
        jumlahPohon = request.POST.get('jumlahPohon')
        pesan = request.POST.get('pesan')
        todo = Donasi.objects.create(nominal=nominal,namaPohon=namaPohon,jumlahPohon=jumlahPohon,pesan=pesan,user=request.user)
        hasil = {
            'fields':{
                'nominal':todo.nominal,
                'namaPohon':todo.namaPohon,
                'jumlahPohon':todo.jumlahPohon,
                'pesan':todo.pesan,
            },
            'pk':todo.pk
        }
        return JsonResponse({"instance":hasil}, status=200)

# @login_required(login_url='login/')
def show_json(request):
    data = Donasi.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")