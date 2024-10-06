import json
from django.core.management.base import BaseCommand
from farm.models import Product

class Command(BaseCommand):
    help = 'Load products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to load')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            products_data = json.load(file)

            for item in products_data:
                product = Product(
                    name=item['name'],
                    description=item['description'],
                    price=item['price'],
                    quantity=item['quantity'],
                    zip=item['zip'],
                    dateHarvested=item['dateHarvested'],
                    businessName=item['businessName']
                )
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
