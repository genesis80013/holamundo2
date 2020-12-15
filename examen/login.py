from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def view(request):
    data = {}
    return render(request, "login.html", data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')