from django.db import models

class WeatherData(models.Model):
    date = models.DateField()
    value = models.FloatField()
    region = models.CharField(max_length=100)
    parameter = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.region} - {self.parameter} - {self.date}"

