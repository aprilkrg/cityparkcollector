from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('parks/', views.ParkList.as_view(), name='parks'),
    path('parks/<int:park_id>', views.parks_detail, name='detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='parks_create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='parks_update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='parks_delete'),

    path('parks/<int:park_id>/add_visit', views.add_visit, name='add_visit'),
    # ^^^ function view for visit creation
    # path('parks/<int:pk>/create_visit', views.VisitCreate.as_view(), name='visit_create'),
    #  ^^^ CBV for visit creation
    path('parks/<int:park_id>/add_photo', views.add_photo, name='add_photo'),

    path('parks/<int:park_id>/assoc_feature/<int:feature_id>/', views.assoc_feature, name='assoc_feature'),
    path('parks/<int:park_id>/unassoc_feature/<int:feature_id>/', views.unassoc_feature, name='unassoc_feature'),

    path('features/', views.FeatureList.as_view(), name='features_index'),
    path('features/<int:pk>/', views.FeatureDetail.as_view(), name='features_detail'),
    path('features/create/', views.FeatureCreate.as_view(), name='features_create'),
    path('features/<int:pk>/update/', views.FeatureUpdate.as_view(), name='features_update'),
    path('features/<int:pk>/delete/', views.FeatureDelete.as_view(), name='features_delete'),
    
    path('accounts/signup/', views.signup, name='signup'),
]