from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30,blank=True)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()