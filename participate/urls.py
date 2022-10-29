from django.urls import path
from participate.views import join_campaign, show_page, show_json

app_name = 'participate'

urlpatterns = [
    path('', show_page, name='show-page'),
    path('json/', show_json, name='show_json'),
    path("add/", join_campaign, name="join_campaign"),
]