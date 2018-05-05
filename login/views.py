from django.shortcuts import render
import requests


def login_function(request):
    return render(request, 'login/login.html')


def get_login_success(request):
    code = request.GET.get('code', None)
    at = requests.get('https://graph.facebook.com/v3.0/oauth/access_token/?client_id=421333258293431&redirect_uri=https://socialfacebook.herokuapp.com/login_success/&client_secret=bf293ff8dc4d986f79da7f36585b26d7&code={}'.format(code)).json()

    context = {
        'at_json': at
    }

    return render(request, 'login/facebook_login_success.html', context)
