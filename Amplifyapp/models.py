from django.db import models

class Song(models.Model):
    title=models.CharField(max_length=10000)
    artist=models.CharField(max_length=10000)
    movie=models.CharField(max_length=10000,blank=True)
    song=models.FileField(upload_to='songs/')
    poster=models.ImageField(upload_to='images/')

    
    def __str__(self):
        return self.title

