from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotdog, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'hotdog-hunter'

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

class HotdogList(LoginRequiredMixin, ListView):
  model = Hotdog

class HotdogDetail(LoginRequiredMixin, DetailView):
  model = Hotdog

class HotdogCreate(LoginRequiredMixin, CreateView):
  model = Hotdog
  fields = ['restaurant', 'location', 'rating', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HotdogUpdate(LoginRequiredMixin, UpdateView):
  model = Hotdog
  fields = ['location', 'rating', 'description']

class HotdogDelete(LoginRequiredMixin, DeleteView):
  model = Hotdog
  success_url = '/hotdogs/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('hotdog-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

@login_required
def add_photo(request, hotdog_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, hotdog_id=hotdog_id)
      hotdog_photo = Photo.objects.filter(hotdog_id=hotdog_id)
      if hotdog_photo.first():
        hotdog_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('hotdog-detail', pk=hotdog_id)