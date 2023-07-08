from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    PARAMS = {"active_page": "dashboard"}
    return render(request, 'home.html', PARAMS)

def accounts(request):
    PARAMS = {"active_page": "accounts"}
    return render(request, 'accounts.html', PARAMS)

def hoardings(request):
    PARAMS = {"active_page": "hoardings"}
    return render(request, 'hoardings.html', PARAMS)

def customers(request):
    PARAMS = {"active_page": "customers"}
    return render(request, 'customers.html', PARAMS)