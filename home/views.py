from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Credential
from django.core.cache import cache
import requests
# Create your views here.


def dashboard(request, username=None):
    s = requests.Session()
    user_id = cache.get('user_id')
    id_token = cache.get('id_token')
    return render(request, 'home/dash.html', {"user_id": user_id, "id_token": id_token})


def loginpage(request):
    print('Serving login page - ')
    return render(request, 'home/login.html')


def authenticate(request, user_name, password):
    try:
        Credential.objects.get(user_name=user_name,password=password)
        return True
    except Credential.DoesNotExist:
        return False