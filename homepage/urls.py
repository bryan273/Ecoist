from django.urls import path, include
from homepage.views import *
app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('submit-question/', submitquestion, name='submitquestion'),
    path('get-campaign-sum/', getcampaignsum, name='getcampaignsum'),
    path('get_last_question/', get_last_question, name="get_last_question"),
    path('flutter-submit-question/', flutter_submitquestion, name='flutter_submitquestion'),
    path('flutter-get-campaign-sum/', flutter_getcampaignsum, name='flutter_getcampaignsum'),
    path('flutter-get_last_question/', flutter_get_last_question, name="flutter_get_last_question"),
    path('flutter-getrecentquestions', flutter_getrecentquestions, name ="flutter_getrecentquestions" ),
    path('json/', show_json, name='show_json'),
]