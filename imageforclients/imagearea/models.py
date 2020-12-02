from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField(max_length=100) 
    images1 = models.ImageField(upload_to='clients/images', default="")

    def __str__(self):
      return self.name