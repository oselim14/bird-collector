from django.urls import reverse
from django.db import models
from datetime import date

TIMES = (
    ('AM', 'Morning'),
    ('PM', 'Afternoon')
)

class Location(models.Model):
  name = models.CharField(max_length=50)
  where = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('locations_detail', kwargs={'pk': self.id})

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    seen_where = models.TextField(max_length=100)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})
    

class Sighting(models.Model):
    date = models.DateField('Sighting Date')
    time = models.CharField(
        max_length=2,
        choices=TIMES,
        default=TIMES[0][0]
    )

    bird = models.ForeignKey(
        Bird, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=250)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for bird_id: {self.bird_id} @{self.url}"