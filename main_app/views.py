from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Park, Feature
from .forms import VisitForm
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def parks_index(request):
    parks = Park.objects.all()
    return render(request, 'parks/index.html', {'parks': parks})

def parks_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    features_park_doesnt_have = Feature.objects.exclude(id__in = park.features.all().values_list('id'))
    visit_form = VisitForm()
    return render(request, 'parks/detail.html', {
        'park': park,
        'visit_form': visit_form,
        'features': features_park_doesnt_have
    })

def assoc_feature(request, park_id, feature_id):
    Park.objects.get(id=park_id).features.add(feature_id)
    return redirect('detail', park_id=park_id)

def add_visit(request, park_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.park_id = park_id
    new_visit.save()
  return redirect('detail', park_id=park_id)

class FeatureList(ListView):
    model = Feature

class FeatureDetail(DetailView):
    model = Feature

class FeatureCreate(CreateView):
    model = Feature
    fields = '__all__'

class FeatureUpdate(UpdateView):
    model = Feature
    fields = ['name']

class FeatureDelete(DeleteView):
    model = Feature
    success_url = '/features/'

class ParkCreate(CreateView):
    model = Park
    fields = '__all__'

class ParkUpdate(UpdateView):
    model = Park
    fields = '__all__'

class ParkDelete(DeleteView):
    model = Park
    success_url = '/parks/'