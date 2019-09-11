from django.db import models

# Create your models here.


class Bookings(models.Model):
    name = models.CharField(max_length=64)
    venue = models.CharField(max_length=128)
    start_time = models.TimeField()
    end_time = models.TimeField()
    secret_code = models.CharField(max_length=10)
