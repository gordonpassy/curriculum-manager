from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Subject

# Create your views here.
def my_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects':subjects})