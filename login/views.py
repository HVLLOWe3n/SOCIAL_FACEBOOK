from django.shortcuts import render
import requests


def login_function(request):
    return render(request, 'login/login.html')
