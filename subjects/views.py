from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Subject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def my_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects':subjects,  'user':request.user})