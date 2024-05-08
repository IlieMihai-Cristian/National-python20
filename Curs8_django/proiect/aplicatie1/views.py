from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie1.models import Location
from django.shortcuts import redirect


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


class UpdateLocationsView(UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


def delete_location(request, pk):
    # SQL nativ: "SELECT id, city FROM aplicatie1_location WHERE id=1"
    # Location.objects.get(id=1).city

    # 1.cu get:
    # instance_object = Location.objects.get(country='Romania')
    # instance_object = Location.objects.get(id=pk)
    # if instance_object.active is True:
    #     instance_object.active = False
    #     instance_object.save()

    # 2.cu filter
    Location.objects.filter(id=pk).update(active=False)
    return redirect('locations:lista_locatii')


def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect('locations:lista_locatii')