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
    path('add/', add_ajax, name='add_ajax'),
    path('add_5/', add_ajax_5, name='add_ajax_5'),
    path('notes/', create_notes, name='create_notes'),
]