import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from admin_ft.models import admin_ft_entry
from campaign.models import Campaign
from donate.models import Donasi
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
from admin_ft.forms import AdminForm

def get_data():
    df_campaign = pd.DataFrame(Campaign.objects.values())
    df_donasi = pd.DataFrame(Donasi.objects.values())
    df_admin = pd.DataFrame(admin_ft_entry.objects.values())
    df_merge = df_admin.merge(df_donasi, how='left',on='user_id').merge(df_campaign, how='left',on='user_id')\
            [['username','nominal','jumlahPohon','namaPohon','pesan','title','description']]
    # df_merge[df_merge.select_dtypes('object').columns] = df_merge[df_merge.select_dtypes('object').columns].fillna("NULL")
    df_merge[['nominal','jumlahPohon']] = df_merge[['nominal','jumlahPohon']].fillna(0).astype(int)
    
    jumlah_campaign = df_merge.groupby("username")['title'].apply(lambda x: x.notnull().sum()).reset_index()
    jumlah_donasi = df_merge.groupby("username")['pesan'].apply(lambda x: x.notnull().sum()).reset_index()
    df_merge = df_merge.groupby('username').agg({'nominal':'sum','jumlahPohon':'sum'}).reset_index()
    df_merge['noted'] = df_admin['noted']
    df_merge['kampanye'] = jumlah_campaign['title']
    df_merge['donasi'] = jumlah_donasi['pesan']
    df_merge = df_merge.reset_index()
    df_merge['index']=df_merge['index']+1
    return df_merge

@login_required(login_url='/admin_ft/login/')
def admin_ft(request):
    plt.figure(facecolor='#dbeafe')
    ax = plt.axes()
    ax.set_facecolor("#dbeafe")
    df = get_data()
    plt.bar(df["username"],df['nominal'])

    fig1 = plt.gcf()
    buf=io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    plt.clf()

    form = AdminForm()
    return render(request, 'admin_ft.html', {'data':uri,'table':df.to_dict('records'),'form':form})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        uname = request.POST.get('username')
        form = UserCreationForm(request.POST)
        print('test')
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            getUser = User.objects.get(username=uname)
            admin_ft_entry.objects.create(user=getUser, username=getUser.username)
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
            if username=='bryan273':
                response = HttpResponseRedirect(reverse("admin_ft:admin_ft")) # membuat response
            else:
                response = HttpResponseRedirect(reverse("#")) # membuat response
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

@login_required(login_url='/admin_ft/login/')
def add_ajax(request):
    df = get_data()
    print(df.to_json())
    return HttpResponse(df.to_json(), content_type="application/json")

@csrf_exempt
def create_notes(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin_obj = admin_ft_entry.objects.filter(username=form.cleaned_data['username'])
            admin_obj.noted = form.cleaned_data['noted']
            admin_obj.save()
            messages.success(request, 'Notes berhasil dibuat')
            # return HTTPResponse(serializers.serialize('json',[admin_obj]),
            #         content_type='application/json',)
        else:
            print('error')
