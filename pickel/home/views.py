from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import CalendarEvent
from .forms import CalendarEventForm

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
    # Fetch all calendar events
    events = CalendarEvent.objects.all()
    return render(request, 'calendar/calendar_view.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.admin_user = request.user  # Assign the current admin user
            event.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm()
    return render(request, 'calendar/add_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id)
    if request.method == 'POST':
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm(instance=event)
    return render(request, 'calendar/edit_event.html', {'form': form, 'event': event})








