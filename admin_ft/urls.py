from django.urls import path
from admin_ft.views import *

app_name = 'admin_ft'

urlpatterns = [
    # path('', show_admin_ft, name="show_admin_ft"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    # path('add/', add_ajax, name='add_ajax'),
]