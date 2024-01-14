from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, reverse
import googlemaps
from .forms import SearchForm
from django.contrib.auth.decorators import login_required

def title(request):
    return render(request, "home/title.html", {})

def queue(request):
    return render(request, "home/queue.html", {})

def beginner_guide(request):
    return render(request, "home/beginner_guide.html")

def watch_pros(request):
    return render(request, "home/watch_pros.html")
  
def calendar_view(request):
    return render(request, 'home/event_calendar.html', {})
  
@csrf_exempt
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            api_key = GOOGLE_API_KEY  # Replace with your actual Google Cloud Platform API key
            search_location = form.cleaned_data['address']
            
            gmaps = googlemaps.Client(key=api_key)

            geocoded = gmaps.geocode(search_location)[0]
            
            geometry = geocoded.get('geometry', {})
            location = geometry.get('location', {})
            lat = location.get('lat')
            long = location.get('lng')

            places_result = gmaps.places_nearby(
                location=(lat, long),
                radius=15000,
                keyword='pickleball court'
            )

            if 'results' in places_result:
                nearest_courts = [
                    {
                        'name': place['name'],
                        'address': place.get('vicinity', 'N/A'),
                        'location': place['geometry']['location']
                    }
                    for place in places_result['results']
                ][:5]  # Take the first 5 results

                return render(request, 'home/search.html', {'nearest_courts': nearest_courts, 'form': form})
            else:
                return JsonResponse({'error': 'No pickleball courts found nearby.'}, status=404)
    else:
        form = SearchForm()

    return render(request, 'home/search.html', {'form': form})






GOOGLE_API_KEY = "put api key here"
