from django.db import models

# Create your models here.

#Register new Client
from django.urls import reverse


class HouseManager(models.Model):
    id_number=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=14)

    def get_absolute_url(self):
        return reverse('administrator:ownerreport',kwargs={'pk':self.pk})


    def __str__(self):
        return self.first_name+'-'+self.last_name
