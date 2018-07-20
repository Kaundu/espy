from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30,blank=True)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()        self.save()


class Categoryy(models.Model):
    name = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =25)
    description = models.TextField
    location = models.ForeignKey(Location,related_name='images')
    category = models.ForeignKey(Categoryy,related_name='images')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
