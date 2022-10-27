from django.urls import path
from donate.views import show_donate

app_name = 'donate'

urlpatterns = [
    path('', show_donate, name='show_donate'),
]