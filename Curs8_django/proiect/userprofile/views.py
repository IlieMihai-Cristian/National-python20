from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.forms import NewAccountForm


class CreateNewAccount(LoginRequiredMixin, CreateView):
    # model = User
    template_name = 'aplicatie1/locations_form.html'
    # fields = ['first_name', 'last_name', 'email', 'username']
    form_class = NewAccountForm

    def get_success_url(self):
        return reverse('locations:lista_locatii')
