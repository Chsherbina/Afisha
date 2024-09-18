from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    def __str__(self):
        return self.title


START = ((star, star*'*') for star in range(1, 6))
class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=START, default=0)
    product = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return self.text