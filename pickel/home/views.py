from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404, render

def title(request):
    return render(request, "templates/home/title.html", {})









