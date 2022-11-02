from django.shortcuts import render
from campaign.models import Campaign
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from campaign.forms import TaskForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def show_campaign(request):
    data = Campaign.objects.all()
    context ={
        'username': "Hatta",
        'campaigns': data,
    }
    return render(request, "campaign.html", context)

@login_required(login_url='/ecoist/login/')
@csrf_exempt
def create_campaign_with_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        campaign = Campaign.objects.create(
            user=request.user,
            title=title,
            description=description,
        )
    return HttpResponse("Success")
        # return JsonResponse(
        #     {   
        #         "pk": campaign.id,
        #         "fields": {
        #             "title": campaign.title,
        #             "description": campaign.description,
        #         },
        #     },
        # )

# def create_campaign(request):
#     form = TaskForm()
#     context = {'form': form}
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form_listener = form.save(commit=False)
#             form_listener.save()
#             return HttpResponseRedirect(reverse('campaign:show_campaign'))
#         else:
#             messages.info(request, 'Terjadi kesalahan saat menyimpan data!')
#     return render(request, 'add_campaign.html', context)

def delete_campaign(request, key):
    campaign = Campaign.objects.get(pk = key)
    campaign.delete()
    return redirect('campaign:show_campaign')

def show_json(request):
    data = Campaign.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")