import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from aplicatie1.models import Location, Pontaj
from django.shortcuts import redirect


# CreateView -> adaugarea datelor noi in baza de date (instante noi)
# ListView -> vizualizarea tuturor datelor dintr-un tabel din baza de date
# DeatailView (pk) -> vizualizarea unei instante specificate dintr-un tabel din baza de date
# UpdateView (pk) -> pentru modificarea datelor dintr-o instanta din baza de date
# DeleteView (pk) -> pentru stergerea definitiva a unei inregistrari din tabel


class LocationsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'
    permission_required = 'aplicatie1.view_location'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super(LocationsView, self).get_context_data(**kwargs)
    #     data['gigel'] = 'Salut'
    #     return data


class CreateLocationsView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationsView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_success_url(self):
        return reverse('locations:lista_locatii')


@login_required
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


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect('locations:lista_locatii')


@login_required
def start_timesheet(request):
    # new_instance = Pontaj()
    # new_instance.user_id = request.user.id
    # new_instance.start_date = datetime.datetime.now()
    # new_instance.save()
    Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
