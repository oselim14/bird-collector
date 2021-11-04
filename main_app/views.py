from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Location
from .forms import SightingForm

# Create your views here.
from django.http import HttpResponse

from main_app import models


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    locations_bird_doesnt_have = Location.objects.exclude(id__in=bird.locations.all().values_list('id'))
    sighting_form = SightingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird,
        'sighting_form': sighting_form, 
        'locations': locations_bird_doesnt_have
    })

class BirdCreate(CreateView):
    model = Bird
    fields = ['name','species', 'description', 'seen_where']

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['species', 'description', 'seen_where']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

def add_sighting(request, bird_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bird_id = bird_id
        new_sighting.save()
    return redirect('detail', bird_id=bird_id)

class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'where']

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'

def assoc_location(request, bird_id, location_id):
    Bird.objects.get(id=bird_id).locations.add(location_id)
    return redirect('detail', bird_id=bird_id)

def unassoc_location(request, bird_id, location_id):
    Bird.objects.get(id=bird_id).locations.remove(location_id)
    return redirect('detail', bird_id=bird_id)