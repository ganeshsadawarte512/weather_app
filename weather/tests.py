from django.test import TestCase
from .models import WeatherData
from datetime import date

class WeatherDataModelTest(TestCase):
    def test_creation(self):
        data = WeatherData.objects.create(
            date=date(2020, 1, 1),
            value=5.2,
            region="UK",
            parameter="Tmax"
        )
        self.assertEqual(str(data), "UK - Tmax - 2020-01-01")

