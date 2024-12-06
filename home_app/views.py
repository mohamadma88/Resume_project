from django.shortcuts import render
from .models import Resume


def home(request):
    resume = Resume.objects.all()
    return render(request, 'home_app/index.html',{'resume':resume})
