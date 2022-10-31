from django.urls import path, include
from homepage.views import show_homepage, submitquestion, getcampaignsum
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('submit-question/', submitquestion, name='submitquestion'),
    path('get-campaign-sum/', getcampaignsum, name='getcampaignsum'),
    path('donate/', include('donate.urls')),
    path('participate/', include('participate.urls')),
    path('campaign/', include('campaign.urls')),
]