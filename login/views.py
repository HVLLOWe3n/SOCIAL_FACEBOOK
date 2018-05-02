from django.shortcuts import render


def login_function(request):
    return render(request, 'login/login.html')
