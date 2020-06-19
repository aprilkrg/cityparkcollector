from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
# FEATURES = (
#     ('w', 'water fountain'),
#     ('s', 'sidewalks'),
#     ('g', 'grassy field'),
#     ('b', 'trashcans'),
#     ('p', 'port-a-potty'),
#     ('t', 'tree shade'),
# )

class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('features_detail', kwards={'pk': self.id})

class Park(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'park_id': self.id})

class Visit(models.Model):
    date = models.DateField('date of Visit')
    comment = models.TextField(max_length=180, default="none")
    
    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} on {self.date}"

        class Meta:
            ordering = ['-date']