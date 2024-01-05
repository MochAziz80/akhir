from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.resonse import Response
from rest_framework.views import APIView, permisions_classes
from rest_framework.authtoken.models import Token



def home(request):
  return HttpResponse ('<h1>Welcome to Home Page</h1>')


def login(request):
  username_login = request.POST.get('username')
  password_login = request.POST.get('password')
  user = authenticate(request, username=username_login, password=password_login)
  if user is not None:
    login(request, user)
    return HttpResponse ('<h1>Login Successful</h1>')
  else:
    return HttpResponse ('<h1>Login Failed</h1>')