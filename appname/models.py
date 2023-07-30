from django.db import models

# Create your models here.
class Comtact(models.Model):
    value = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pho = models.CharField(max_length=50)
    decs = models.CharField(max_length=600)
    date = models.DateField()

    def __str__(self):
        return self.value
    