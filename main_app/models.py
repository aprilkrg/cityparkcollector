from django.db import models
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import date


class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('features_detail', kwargs={'pk': self.id})

class Park(models.Model):  
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    features = models.ManyToManyField(Feature)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'park_id': self.id})

class Visit(models.Model):
    date = models.DateField('Date of Visit')
    comment = models.TextField(max_length=180, default='none')
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.comment} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for park_id: {self.park_id} @{self.url}"