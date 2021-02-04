from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Video

def index(request):
    latest_video_list = Video.objects.order_by('-add_date')[:5]
    template = loader.get_template('video/index.html')
    context = {
        'latest_video_list': latest_video_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, video_id):
    return HttpResponse("You're looking at video %s." % video_id)