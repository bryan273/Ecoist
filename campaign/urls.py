from django.urls import path
from campaign.views import show_campaign, create_campaign_with_ajax, create_campaign, delete_campaign, show_json

app_name = 'campaign'

urlpatterns = [
    path('', show_campaign, name='show_campaign'),
    path('createcampaign/', create_campaign,  name='create_campaign'),
    path('delete_campaign/<str:key>/', delete_campaign, name='delete_campaign'),
    path('json/', show_json, name='show_json'),
]