from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def title(request):
    return render(request, "home/title.html", {})

def queue(request):
    return render(request, "home/queue.html", {})

def beginner_guide(request):
    return render(request, "home/beginner_guide.html")

def watch_pros(request):
    return render(request, "home/watch_pros.html")

#calendar stuff

def calendar_view(request):
    return render(request, 'home/event_calendar.html', {})








