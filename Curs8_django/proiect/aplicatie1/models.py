from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.country} -> {self.city}'


class Pontaj(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user} started at: {self.start_date}'


class Logs(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
