from django.urls import path
from campaign.views import show_campaign, create_campaign_with_ajax, show_json, delete_campaign

app_name = 'campaign'

urlpatterns = [
    path('', show_campaign, name='show_campaign'),
    path('delete_campaign/<str:key>/', delete_campaign, name='delete_campaign'),
    path('json/', show_json, name='show_json'),
    path('createajax/', create_campaign_with_ajax, name='create_campaign_with_ajax'),
]