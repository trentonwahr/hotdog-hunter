from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('hotdogs/', views.HotdogList.as_view(), name='hotdog-index'),
  path('hotdogs/<int:pk>/', views.HotdogDetail.as_view(), name='hotdog-detail'),
  path('hotdogs/create/', views.HotdogCreate.as_view(), name='hotdog-create'),
  path('hotdogs/<int:pk>/update/', views.HotdogUpdate.as_view(), name='hotdog-update'),
  path('hotdogs/<int:pk>/delete/', views.HotdogDelete.as_view(), name='hotdog-delete'),
  path('hotdogs/<int:hotdog_id>/add-photo/', views.add_photo, name='add-photo'),
  path('accounts/signup/', views.signup, name='signup'),
]