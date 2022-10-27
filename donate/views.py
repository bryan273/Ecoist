from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
# @login_required(login_url='ecoist/login/')
def show_donate(request):
    username = request.user
    context = {
        'user': username
    }
    return render(request, "donate.html", context)

# @login_required(login_url='/login/')
def input_donasi(request):
    if request.method == 'POST':
        nominal = request.POST.get('nominal')
        pohon = request.POST.get('pohon')
        pesan = request.POST.get('pesan')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'donate.html', context)