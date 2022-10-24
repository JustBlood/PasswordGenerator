from django.shortcuts import render
from .forms import MyPasswordForm
import random

def index(request):
    return render(request, 'generator/home.html', {'title':'Home Page'})

def generator_view(request):
    passForm = MyPasswordForm()
    return render(request, 'generator/generator.html', {'title':'Generator','form': passForm})

def pass_view(request):
    password = ''

    # By default password characters
    characters = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '!@#$%^&*(){}:"|<>?,.~`\\\''
    numbers = '0123456789'
    # By default length password
    length = 10

    # for POST requests
    if 'length' in request.POST.keys():
        length = int(request.POST['length'])
    if 'uppercase' in request.POST.keys():
        characters += characters.upper()
    if 'numbers' in request.POST.keys():
        characters += numbers
    if 'special' in request.POST.keys():
        characters += special_characters
    # for GET request (version 2)
    if request.GET.get('length'):
        length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters += characters.upper()
    if request.GET.get('numbers'):
        characters += numbers
    if request.GET.get('special'):
        characters += special_characters

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'title':'Your password','password':password})

def about_view(request):
    return render(request, 'generator/about.html', {'title':'Creator page'})
