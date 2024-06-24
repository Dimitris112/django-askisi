from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("AUTO EDW THA HTAN TO ABOUT PAGE")