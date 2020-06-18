from django.db import models
from django.urls import reverse

# Create your models here.
FEATURES = (
    ('w', 'water fountain'),
    ('s', 'sidewalks'),
    ('g', 'grassy field'),
    ('b', 'trashcans'),
    ('p', 'port-a-potty'),
    ('t', 'tree shade'),
)

class Park(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'park_id': self.id})

class Visit(models.Model):
    date = models.DateField('date of Visit')
    feature = models.CharField(
        max_length=1,
        choices=FEATURES,
        default=FEATURES[0][0]
    )
    
    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_feature_display()} on {self.date}"

        class Meta:
            ordering = ['-date']