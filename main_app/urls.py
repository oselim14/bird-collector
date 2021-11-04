from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'),
    path('birds/<int:bird_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('birds/<int:bird_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
    path('birds/<int:bird_id>/unassoc_location/<int:location_id>/', views.unassoc_location, name='unassoc_location'),
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete')
]