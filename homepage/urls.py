from django.urls import path, include
from homepage.views import show_homepage, submitquestion, getcampaignsum, get_last_question, show_json
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('submit-question/', submitquestion, name='submitquestion'),
    path('get-campaign-sum/', getcampaignsum, name='getcampaignsum'),
    path('get_last_question/', get_last_question, name="get_last_question"),
    path('json/', show_json, name='show_json'),
]