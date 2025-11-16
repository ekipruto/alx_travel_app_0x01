from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seeds the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach House", "description": "Beautiful view", "location": "Mombasa", "price_per_night": 12000},
            {"title": "Nairobi Apartment", "description": "Close to City Center", "location": "Nairobi", "price_per_night": 5000},
            {"title": "Maasai Mara Camp", "description": "Wildlife adventure", "location": "Narok", "price_per_night": 8000},
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Sample listings seeded successfully ✔"))
