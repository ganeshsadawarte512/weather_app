import requests
from django.core.management.base import BaseCommand
from weather.models import WeatherData
from datetime import datetime

class Command(BaseCommand):
    help = 'Parse MetOffice weather data and save to DB'

    def handle(self, *args, **kwargs):
        url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt'
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data"))
            return

        lines = response.text.splitlines()[7:]

        for line in lines:
            if not line.strip():
                continue
            parts = line.split()
            year = parts[0]
            for month, val in enumerate(parts[1:13], start=1):
                if val == "---":
                    continue
                WeatherData.objects.get_or_create(
                    date=datetime(int(year), month, 1),
                    value=float(val),
                    region='UK',
                    parameter='Tmax'
                )

        self.stdout.write(self.style.SUCCESS("Data parsed and saved!"))
