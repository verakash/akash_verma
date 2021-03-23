from django.db import models

# Create your models here.

class testmodels(models.Model):
    Name = models.CharField(max_length= 20)
    Age= models.IntegerField(max_length= 3)

    def __str__(self):
        return self.Name
