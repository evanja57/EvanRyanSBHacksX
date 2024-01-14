from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('home/', views.title, name='home'),

    path('queue/', views.queue, name='queue'),
]


















