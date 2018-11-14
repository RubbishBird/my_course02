from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'username':'鲁班'
    }
    return render(request,'index.html',context=context)

def company(request):
    return render(request,'company.html')

def school(request):
    return render(request,'school.html')