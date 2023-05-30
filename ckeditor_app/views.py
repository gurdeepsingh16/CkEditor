from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    if request.method == "GET":
        form = ck_forms()
        return render(request,'home.html',{'form':form})
    else:
        form = ck_forms(request.POST)
        form.save()
        return render(request,'home.html')