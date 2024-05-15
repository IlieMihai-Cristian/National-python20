from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):  #forms.Form

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Introduceti Numele', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Introduceti Prenumele', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Introduceti Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Introduceti Username', 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        email_data = cleaned_data.get('email')
        if User.objects.filter(email=email_data).exists():
            msg = 'Emailul deja exista!'
            self._errors['email'] = self.error_class([msg])
        return cleaned_data
