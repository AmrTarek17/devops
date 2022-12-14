from django.db import models


# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField(default=100)


    def __str__(self):
        return f"{self.name}"
