from django.urls import path
from .views import calendar_view

from . import views

app_name = "home"

urlpatterns = [
    path('home/', views.title, name='home'),
    path('queue/', views.queue, name='queue'),
    path('beginner-guide/', views.beginner_guide, name='beginner_guide'),
    path('watch-pros/', views.watch_pros, name='watch_pros'),
    path('calendar/', calendar_view, name='calendar_view'),
    path('chatbot', views.chatbot, name="chatbot")
]


















