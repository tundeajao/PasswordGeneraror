from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here
def home(request):
    return render(request, 'generator/home.html', {'password' : '53ecsf@wtgvw%&1fwVF'})

def about(request):
    return render(request, 'generator/about.html', {'password' : '53ecsf@wtgvw%&1fwVF'})

def password(request):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(letters)

    thepassword=''

    if request.GET.get('uppercase'):
        characters.extend(list(letters.upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length=int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})
