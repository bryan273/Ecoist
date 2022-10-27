import datetime
from django.shortcuts import render, redirect
from admin_ft.models import admin_ft_entry
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# @login_required(login_url='login/')
# def show_admin_ft(request):
#     data_todo = admin_ftEntry.objects.filter(user=request.user)

#     context = {
#     'list_todo': data_todo,
#     'nama': 'Bryan Tjandra',
#     'username' :  request.user.username,
#     }
#     return render(request, "admin_ft.html",context=context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('admin_ft:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("admin_ft:show_admin_ft")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('admin_ft:login'))
    response.delete_cookie('last_login')
    return response

# @login_required(login_url='/admin_ft/login/')
# def add_ajax(request):
#     if request.method == 'POST':
#         title = request.POST.get('nama')
#         description = request.POST.get('desc')
#         is_finished = False
#         todo = admin_ftEntry.objects.create(title=title, 
#                                             description=description,
#                                             date=datetime.date.today(), 
#                                             user=request.user,
#                                             is_finished=is_finished)
#         todo.save()
        
#         result = {
#             'fields':{
#                 'title':todo.title,
#                 'description':todo.description,
#                 'is_finished':todo.is_finished,
#                 'date':todo.date,
#             },
#             'pk':todo.pk
#         }
#         return JsonResponse(result,status=200)