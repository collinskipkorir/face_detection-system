from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.BigIntegerField()
    email = models.EmailField()
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

