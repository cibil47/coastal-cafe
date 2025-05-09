import json
import sys
from django.core.management.base import BaseCommand
from kitchen.models import Food, FoodCategory

CATEGORY_KEYWORDS = [
    "Burger", "Pizza", "Sandwich", "Wrap", "Shawarma", "Momos", "Noodles", "Fried Rice",
    "Soup", "Pasta", "Fries", "Milk Shake", "Juice", "Ice Cream", "Falooda", "Muffin",
    "Lassi", "Mojito", "Brownie", "Combo", "Toast", "Popcorn", "Frappuccino", "Soda",
    "Meal", "Platter"
]

def find_category(food_name):
    for keyword in CATEGORY_KEYWORDS:
        if keyword.lower() in food_name.lower():
            return keyword
    return None

class Command(BaseCommand):
    help = 'Load food items from a JSON file. Usage: python manage.py load_food_items <file.json>'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the food items JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            with open(file_path, 'r') as file:
                food_data = json.load(file)
        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")
            return
        except json.JSONDecodeError:
            self.stderr.write("Invalid JSON format")
            return

        for entry in food_data:
            name = entry.get('food_name')
            price = entry.get('food_price')

            if not name or price is None:
                continue

            category_name = find_category(name)
            category_obj = None

            if category_name:
                category_obj, _ = FoodCategory.objects.get_or_create(name=category_name)

            food, created = Food.objects.get_or_create(
                name=name,
                defaults={
                    'price': int(price),
                    'category': category_obj
                }
            )
            if created:
                self.stdout.write(f"Loaded: {name}")
            else:
                self.stdout.write(f"Skipped (already exists): {name}")

