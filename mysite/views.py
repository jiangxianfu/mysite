from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
import os
# Create your views here.
def index(request):
    return render(request,"index.html",{'user':'jiangxf' })