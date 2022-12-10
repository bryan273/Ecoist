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
import json

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
@csrf_exempt
def flutter_top_donations(request):
    df_don, _ = get_data()
    
    print(df_don[['username','nominal']][:5].to_dict('records'))

    return HttpResponse(json.dumps({'don_top_5':df_don[['username','nominal']][:5].to_dict('records')}), 
                        content_type='application/json')

@csrf_exempt
def flutter_top_campaigns(request):
    _, df_par = get_data()
    
    print(df_par[['username','kampanye']][:5].to_dict('records'))

    return HttpResponse(json.dumps({'par_top_5':df_par[['username','kampanye']][:5].to_dict('records')}), 
                        content_type='application/json')

@csrf_exempt
def flutter_dist_donations(request):
    df_don, _ = get_data()
    
    print(df_don[['nominal']].to_dict('records'))

    return HttpResponse(json.dumps({'don_dist':df_don[['nominal']].to_dict('records')}), 
                        content_type='application/json')

@csrf_exempt
def flutter_dist_campaigns(request):
    _, df_par = get_data()
    
    print(df_par[['kampanye']].to_dict('records'))

    return HttpResponse(json.dumps({'par_dist':df_par[['kampanye']].to_dict('records')}), 
                        content_type='application/json')

@csrf_exempt
def flutter_top_user(request):
    
    print('masuk ke views django')
    df_don, _ = get_data()
    
    print(df_don[:5].astype(str).to_dict('records'))

    return HttpResponse(json.dumps({'table_top_5':df_don[:5].to_dict('records')}), 
                        content_type='application/json')

@csrf_exempt
def register(request):
    form = UserCreationForm()
    print(admin_ft_entry.objects.all().values)
    uname = request.POST.get('username')
    form = UserCreationForm(request.POST)
    print('test')
    if form.is_valid():
        form.save()
        messages.success(request, 'Akun telah berhasil dibuat!')
        getUser = User.objects.get(username=uname)
        admin_ft_entry.objects.create(user=getUser, username=getUser.username)
        return redirect('admin_ft:login')
    else :
        print(uname)
        return JsonResponse({
            "status": False,
            "message": "Failed to Register."
        }, status=401)

@csrf_exempt
def flutter_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        is_user_already_exist = User.objects.filter(username=username).exists()
        if (username == '') or (password_1 == '') or (password_2 ==''):
            return JsonResponse({
              "status": False,
              "message": "Teks tidak boleh kosong"
            }, status=401)
        elif (len(password_1)<=5):
            return JsonResponse({
              "status": False,
              "message": "Panjang password harus lebih dari 5"
            }, status=401)
        elif (password_1!=password_2):
            return JsonResponse({
              "status": False,
              "message": "Password harus sama"
            }, status=401)
        elif (not is_user_already_exist) and (password_1==password_2):
            user = User.objects.create_user(username=username,password=password_1)
            user.save()
            admin_ft_entry.objects.create(user=user, username=username)
            return JsonResponse({
                "status": True,
                "username": user.username,
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Username sudah terdaftar"
            }, status=401)
    else:
        return JsonResponse({
            "status": "Password error"
        }, status=401)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        isAdmin = False
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            if username=='admin_ecoist':
                response = HttpResponseRedirect(reverse("admin_ft:admin_ft")) # membuat response
                isAdmin = True
            else:
                response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                'isAdmin': isAdmin,
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            messages.info(request, 'Username atau Password salah!')
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, check your email/password."
            }, status=401)
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def flutter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        isAdmin = False
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            if username=='admin_ecoist':
                isAdmin = True
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                'isAdmin': isAdmin,
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, check your email/password."
            }, status=401)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('admin_ft:login'))
    response.delete_cookie('last_login')
    return JsonResponse({
            "status": True,
            "message": "Successfully Register!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)

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