from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationsView.as_view(), name='adaugare'),
]
