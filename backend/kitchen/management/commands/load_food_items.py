import json
from django.core.management.base import BaseCommand
from kitchen.models import Food

class Command(BaseCommand):
    help = 'Load food items from a JSON file into the Food model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to food_items.json')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            for item in data:
                name = item.get('food_name')
                price = item.get('food_price')
                if name and price is not None:
                    Food.objects.get_or_create(name=name, price=price)
                    self.stdout.write(self.style.SUCCESS(f"Loaded: {name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Skipped incomplete item: {item}"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {json_file}"))
        except json.JSONDecodeError:
            self.stderr.write(self.style.ERROR("Invalid JSON format"))

