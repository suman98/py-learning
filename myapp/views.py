from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World! from suman")
