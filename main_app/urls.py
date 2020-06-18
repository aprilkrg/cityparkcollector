from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('parks/', views.parks_index, name='parks'),
    path('parks/<int:park_id>', views.parks_detail, name='detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='parks_create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='parks_update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='parks_delete'),
    path('parks/<int:park_id>/add_visit', views.add_visit, name='add_visit'),
]