from django.urls import path
from .views import calendar_view, add_event, edit_event

from . import views

app_name = "home"

urlpatterns = [
    path('home/', views.title, name='home'),
    path('queue/', views.queue, name='queue'),
    path('beginner-guide/', views.beginner_guide, name='beginner_guide'),
    path('watch-pros/', views.watch_pros, name='watch_pros'),
    path('calendar/', calendar_view, name='calendar_view'),
    path('calendar/add/', add_event, name='add_event'),
    path('calendar/edit/<int:event_id>/', edit_event, name='edit_event'),
]


















