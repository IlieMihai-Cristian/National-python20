from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from aplicatie1.models import Location


# CreateView -> adaugarea datelor noi in baza de date (instante noi)
# ListView -> vizualizarea tuturor datelor dintr-un tabel din baza de date
# DeatailView (pk) -> vizualizarea unei instante specificate dintr-un tabel din baza de date
# UpdateView (pk) -> pentru modificarea datelor dintr-o instanta din baza de date
# DeleteView (pk) -> pentru stergerea definitiva a unei inregistrari din tabel


class LocationsView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'


class CreateLocationsView(CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


