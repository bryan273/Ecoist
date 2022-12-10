from django.urls import path
from admin_ft.views import *

app_name = 'admin_ft'

urlpatterns = [
    # path('', show_admin_ft, name="show_admin_ft"),
    path('register/', register, name='register'),
    path('flutter_register/', flutter_register, name='flutter_register'), 
    path('flutter_login/', flutter_login, name='flutter_login'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('admin_ft/', admin_ft, name='admin_ft'),
    path('flutter_top_user/', flutter_top_user, name='flutter_top_user'),
    path('flutter_top_donations/', flutter_top_donations, name='flutter_top_donations'),
    path('flutter_top_campaigns/', flutter_top_campaigns, name='flutter_top_campaigns'),
    path('flutter_dist_donations/', flutter_dist_donations, name='flutter_dist_donations'),
    path('flutter_dist_campaigns/', flutter_dist_campaigns, name='flutter_dist_campaigns'),
    path('add/', add_ajax, name='add_ajax'),
    path('add_5/', add_ajax_5, name='add_ajax_5'),
    path('notes/', create_notes, name='create_notes'),
]