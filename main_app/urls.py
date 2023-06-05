from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('hotdogs/', views.HotdogList.as_view(), name='hotdog-index'),
  path('hotdogs/<int:pk>/', views.HotdogDetail.as_view(), name='hotdog-detail'),
  path('hotdogs/create/', views.HotdogCreate.as_view(), name='hotdog-create'),
]