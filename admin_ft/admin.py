from django.contrib import admin
from admin_ft.models import admin_ft_entry
from campaign.models import Campaign
from donate.models import Donasi

admin.site.register(admin_ft_entry)
admin.site.register(Campaign)
admin.site.register(Donasi)