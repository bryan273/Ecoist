from django.urls import path
from donate.views import *

app_name = 'donate'

urlpatterns = [
    path('', show_donate, name='show_donate'),
    path('json/', show_json, name='show_json'),
    path('donate_ajax/', donate_ajax, name='donate_ajax'),
    path('flutter_donation/', flutter_donation, name='flutter_donation'),
]