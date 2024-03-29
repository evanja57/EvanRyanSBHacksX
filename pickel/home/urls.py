from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('home/', views.title, name='home'),
    path('queue/', views.queue, name='queue'),
    path('search/', views.search, name='search'),
    path('beginner-guide/', views.beginner_guide, name='beginner_guide'),
    path('watch-pros/', views.watch_pros, name='watch_pros'),
    path('calendar/', views.calendar_view, name='calendar_view'),
]


















