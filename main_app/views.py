from django import http
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Bird():
    def __init__(self, name, species, description, seen_where):
        self.name = name,
        self.species = species,
        self.description = description,
        self.seen_where = seen_where

birds = [
    Bird('Bird 1', 'Robin', 'friendly', 'backyard'),
    Bird('Bird 2', 'Blue Jay', 'friendly', 'front yard'),
    Bird('Bird 3', 'Woodpecker', 'not friendly', 'tree in back yard'),
]


def home(request):
    return HttpResponse('<h1>Hello smol birbs</h1>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', {'birds': birds})
    