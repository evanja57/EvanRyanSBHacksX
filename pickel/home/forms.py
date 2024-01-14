from django import forms
from .models import CalendarEvent

# Create your calendar forms here.

class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'date', 'description']




















