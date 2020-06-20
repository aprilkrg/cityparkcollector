from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Park, Feature, Photo
from .forms import VisitForm

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'cityparkcollector-bucket'

def add_photo(request, park_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to park_id or park (if you have a park object)
            photo = Photo(url=url, park_id=park_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', park_id=park_id)

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

