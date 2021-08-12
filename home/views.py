from django.http import HttpResponse
from django.shortcuts import render
from .models import  Job


# Create your views here.
def welcome(request):

    return render(request, "home/homepage.html")

def jobs(request):
    context =Job.objects.all()
    return render(request,"home/jobs.html", {'ctx':context})
