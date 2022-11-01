import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from admin_ft.models import admin_ft_entry
from campaign.models import Campaign
from donate.models import Donasi
from participate.models import Participants
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
import seaborn as sns

def get_data():
    df_participant = pd.DataFrame(Participants.objects.values())
    df_donasi = pd.DataFrame(Donasi.objects.values())
    df_admin = pd.DataFrame(admin_ft_entry.objects.values())

    df_par = pd.merge(df_admin, df_participant, on='user_id',how='left')\
                [['user_id','username','noted','campaign_id']]
    df_don = pd.merge(df_admin, df_donasi, on='user_id', how='left')
    df_par.rename(columns={'campaign_id':'title'}, inplace=True)
    df_don.rename(columns={'campaign_id':'title'}, inplace=True)
    # df_merge[df_merge.select_dtypes('object').columns] = df_merge[df_merge.select_dtypes('object').columns].fillna("NULL")
    df_don[['nominal','jumlahPohon']] = df_don[['nominal','jumlahPohon']].fillna(0).astype(int)
    
    jumlah_campaign = df_don.groupby("username")['title'].apply(lambda x: x.notnull().sum()).reset_index()
    jumlah_donasi = df_don.groupby("username")['pesan'].apply(lambda x: x.notnull().sum()).reset_index()
    df_don = df_don.groupby(['username','user_id']).agg({'nominal':'sum','jumlahPohon':'sum'}).reset_index()
    df_don['kampanye'] = jumlah_campaign['title']
    df_don['donasi'] = jumlah_donasi['pesan']
    df_don= pd.merge(df_don, df_admin[['user_id','noted']], on='user_id')
    df_don = df_don.sort_values(by='nominal',ascending=False).reset_index()
    df_don['index']=list(range(1,df_don.shape[0]+1))

    df_par = df_par.groupby("username")['title'].apply(lambda x: x.notnull().sum()).reset_index()
    df_par.columns =['username','kampanye']
    df_par = df_par.sort_values(by='kampanye',ascending=False).reset_index()
    df_par['index']=list(range(1,df_par.shape[0]+1))
    # print(df_merge)
    return df_don, df_par

def encode_png():
    fig1 = plt.gcf()
    buf=io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.clf()
    return uri

@login_required(login_url='/admin_ft/login/')
def admin_ft(request):
    plt.figure(facecolor='#dbeafe')
    ax = plt.axes()
    ax.set_facecolor("#dbeafe")

    df_don, df_par = get_data()
    sns.set(style="whitegrid", color_codes=True)
    plt.title('Top 5 Donations')
    pal = sns.color_palette("Greens_d", df_don.shape[0])
    sns.barplot(x="username",y='nominal', data=df_don[:5],palette=pal[::-1])
    uri = encode_png()

    plt.figure(facecolor='#dbeafe')
    ax = plt.axes()
    ax.set_facecolor("#dbeafe")
    sns.set(style="whitegrid", color_codes=True)
    plt.title('Top 5 Campaigns')
    sns.barplot(x='username',y='kampanye',data=df_par[:5], palette='rocket', ci=None)
    uri2 = encode_png()

    plt.figure(facecolor='#dbeafe')
    ax = plt.axes()
    ax.set_facecolor("#dbeafe")
    sns.set(style="whitegrid", color_codes=True)
    plt.title('Donation Distribution')
    plt.xlim(0,100000)
    sns.distplot(df_don.nominal)
    uri3 = encode_png()

    plt.figure(facecolor='#dbeafe')
    ax = plt.axes()
    ax.set_facecolor("#dbeafe")
    sns.set(style="whitegrid", color_codes=True)
    plt.title('Campaign Distribution')
    plt.xlim(0,6)
    sns.distplot(df_par.kampanye)
    uri4 = encode_png()

    form = AdminForm()
    return render(request, 'admin_ft.html', 
                            {'top_5_donation':uri,
                            'top_5_campaign':uri2,
                            'dist_donation':uri3,
                            'dist_kampanye':uri4,
                            'form':form,
                            'table_top_5':df_don[:5].to_dict('records')})

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
            if username=='admin_ecoist':
                response = HttpResponseRedirect(reverse("admin_ft:admin_ft")) # membuat response
            else:
                response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
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
    df_don,df_par = get_data()
    print(df_don.to_json())
    return HttpResponse(df_don.to_json(), content_type="application/json")

@login_required(login_url='/admin_ft/login/')
def add_ajax_5(request):
    df_don,df_par = get_data()
    return HttpResponse(df_don[:5].to_json(), content_type="application/json")

@csrf_exempt
def create_notes(request):
    form = AdminForm(request.POST)
    if request.method == 'POST':
        # print(form)
        # if form.is_valid():
        print(dir(form))
        print(request.POST.get('nama'))
        user = User.objects.get(username = request.POST.get('nama'))
        admin_obj = admin_ft_entry.objects.get(user=user)
        admin_obj.noted = request.POST.get('note')
        admin_obj.save()
        # print(pd.DataFrame(admin_ft_entry.objects.values()))
        messages.success(request, 'Notes berhasil dibuat')
        return JsonResponse({"instance":'proyek dibuat'}, status=200)
        # else:
        #     print('error')
