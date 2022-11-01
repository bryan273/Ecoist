from django.urls import path
from donate.views import show_donate
from donate.views import show_json
from donate.views import donate_ajax

app_name = 'donate'

urlpatterns = [
    path('', show_donate, name='show_donate'),
    path('json/', show_json, name='show_json'),
    path('donate_ajax/', donate_ajax, name='donate_ajax'),
]