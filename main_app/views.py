from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotdog

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

class HotdogList(ListView):
  model = Hotdog

class HotdogDetail(DetailView):
  model = Hotdog

class HotdogCreate(CreateView):
  model = Hotdog
  fields = ['restaurant', 'location', 'rating', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HotdogUpdate(UpdateView):
  model = Hotdog
  fields = ['location', 'rating', 'description']

class HotdogDelete(DeleteView):
  model = Hotdog
  success_url = '/hotdogs/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dog-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)