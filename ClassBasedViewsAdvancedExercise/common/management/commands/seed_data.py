from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from destinations.models import Destination
from reviews.models import Review
from travelers.models import Traveler


TRAVELERS = [
    ("Maria Petrova", "maria.petrova@university.com", 22, "BG"),
    ("James Carter", "james.carter@university.org", 27, "UK"),
    ("Lena Schmidt", "lena.schmidt@university.com", 24, "DE"),
    ("Camille Dubois", "camille.dubois@university.org", 31, "FR"),
    ("Luca Romano", "luca.romano@university.com", 19, "IT"),
    ("Sofia Garcia", "sofia.garcia@university.org", 26, "ES"),
    ("Ethan Miller", "ethan.miller@university.com", 35, "US"),
    ("Olivia Tremblay", "olivia.tremblay@university.org", 29, "CA"),
    ("Jack Wilson", "jack.wilson@university.com", 23, "AU"),
    ("Georgi Ivanov", "georgi.ivanov@university.org", 41, "BG"),
    ("Aiko Tanaka", "aiko.tanaka@university.com", 25, "OTHER"),
    ("Hannah Becker", "hannah.becker@university.org", 18, "DE"),
]

DESTINATIONS = [
    ("Rila Monastery", "BG", "45.00", True,
     "UNESCO-listed Orthodox monastery nestled in the Rila Mountains, famous for its frescoes."),
    ("Seven Rila Lakes", "BG", "60.00", True,
     "A chain of glacial lakes offering one of the most scenic day hikes in the Balkans."),
    ("Edinburgh Old Town", "UK", "120.50", True,
     "Medieval streets, the Royal Mile and a castle perched on an extinct volcano."),
    ("Neuschwanstein Castle", "DE", "95.00", True,
     "The fairy-tale castle in the Bavarian Alps that inspired countless storybook illustrations."),
    ("Mont Saint-Michel", "FR", "110.00", True,
     "A tidal island abbey rising dramatically from the bay between Normandy and Brittany."),
    ("Amalfi Coast", "IT", "250.00", True,
     "Cliffside villages, lemon groves and turquoise water along the Sorrentine Peninsula."),
    ("Sagrada Familia", "ES", "75.00", True,
     "Gaudi's unfinished basilica in Barcelona, a masterpiece of modernist architecture."),
    ("Grand Canyon", "US", "180.00", True,
     "Mile-deep canyon carved by the Colorado River with breathtaking sunrise viewpoints."),
    ("Banff National Park", "CA", "210.00", True,
     "Rocky Mountain peaks, glaciers and the iconic turquoise waters of Lake Louise."),
    ("Great Barrier Reef", "AU", "320.00", True,
     "The world's largest coral reef system, perfect for snorkeling and diving."),
    ("Kyoto Temples", "OTHER", "140.00", True,
     "Thousands of shrines and temples, including the golden Kinkaku-ji pavilion."),
    ("Venice Canals", "IT", "199.99", False,
     "Gondola rides through historic canals - currently closed for seasonal maintenance."),
]

# destination name -> traveler emails who visited it
VISITS = {
    "Rila Monastery": ["maria.petrova@university.com", "georgi.ivanov@university.org", "lena.schmidt@university.com"],
    "Seven Rila Lakes": ["maria.petrova@university.com", "georgi.ivanov@university.org", "james.carter@university.org"],
    "Edinburgh Old Town": ["james.carter@university.org", "olivia.tremblay@university.org"],
    "Neuschwanstein Castle": ["lena.schmidt@university.com", "hannah.becker@university.org", "aiko.tanaka@university.com"],
    "Mont Saint-Michel": ["camille.dubois@university.org", "luca.romano@university.com"],
    "Amalfi Coast": ["luca.romano@university.com", "sofia.garcia@university.org", "ethan.miller@university.com"],
    "Sagrada Familia": ["sofia.garcia@university.org", "camille.dubois@university.org", "jack.wilson@university.com"],
    "Grand Canyon": ["ethan.miller@university.com", "olivia.tremblay@university.org"],
    "Banff National Park": ["olivia.tremblay@university.org", "ethan.miller@university.com", "hannah.becker@university.org"],
    "Great Barrier Reef": ["jack.wilson@university.com", "aiko.tanaka@university.com"],
    "Kyoto Temples": ["aiko.tanaka@university.com", "maria.petrova@university.com"],
    "Venice Canals": ["luca.romano@university.com", "camille.dubois@university.org"],
}

# (traveler email, destination name, rating, type, verified, body)
REVIEWS = [
    ("maria.petrova@university.com", "Rila Monastery", "4.80", "Text", True,
     "Absolutely stunning frescoes and a peaceful atmosphere. Go early to avoid the crowds."),
    ("georgi.ivanov@university.org", "Seven Rila Lakes", "5.00", "Video", True,
     "Filmed the whole hike - the view from the top over all seven lakes is unreal."),
    ("james.carter@university.org", "Edinburgh Old Town", "4.20", "Text", False,
     "Great history and pubs, but bring an umbrella. The castle tour is worth it."),
    ("lena.schmidt@university.com", "Neuschwanstein Castle", "4.50", "Audio", True,
     "Book tickets in advance. Marienbrucke gives the best photo of the castle."),
    ("camille.dubois@university.org", "Mont Saint-Michel", "4.70", "Text", True,
     "Watching the tide come in was magical. Stay overnight for a quieter experience."),
    ("luca.romano@university.com", "Amalfi Coast", "4.90", "Video", False,
     "Positano at sunset is a dream. The bus rides are hair-raising though!"),
    ("sofia.garcia@university.org", "Sagrada Familia", "5.00", "Text", True,
     "The light through the stained glass is breathtaking. A must-see in Barcelona."),
    ("ethan.miller@university.com", "Grand Canyon", "4.60", "Audio", False,
     "Hiked part of Bright Angel Trail. Bring lots of water - it gets hot fast."),
    ("olivia.tremblay@university.org", "Banff National Park", "4.95", "Video", True,
     "Lake Louise and Moraine Lake look photoshopped in real life. Incredible."),
    ("jack.wilson@university.com", "Great Barrier Reef", "4.40", "Text", True,
     "Saw turtles and reef sharks while snorkeling. Some coral bleaching was sad to see."),
    ("aiko.tanaka@university.com", "Kyoto Temples", "4.85", "Text", True,
     "Fushimi Inari at dawn is unforgettable. Wear comfortable shoes."),
    ("hannah.becker@university.org", "Neuschwanstein Castle", "3.90", "Text", False,
     "Beautiful outside, but the interior tour felt rushed and very crowded."),
    ("james.carter@university.org", "Seven Rila Lakes", "4.30", "Audio", False,
     "Challenging but rewarding hike. The chairlift saves a lot of time."),
]


class Command(BaseCommand):
    help = "Seed the database with sample travelers, destinations and reviews."

    @transaction.atomic
    def handle(self, *args, **options):
        travelers = {}
        for name, email, age, country in TRAVELERS:
            traveler, _ = Traveler.objects.get_or_create(
                email=email,
                defaults={"name": name, "age": age, "country": country},
            )
            travelers[email] = traveler

        destinations = {}
        for name, country, price, is_available, description in DESTINATIONS:
            destination, _ = Destination.objects.get_or_create(
                name=name,
                country=country,
                defaults={
                    "price": Decimal(price),
                    "is_available": is_available,
                    "description": description,
                },
            )
            destinations[name] = destination

        for destination_name, emails in VISITS.items():
            destinations[destination_name].travelers.add(*(travelers[e] for e in emails))

        for email, destination_name, rating, review_type, is_verified, body in REVIEWS:
            Review.objects.get_or_create(
                traveler=travelers[email],
                destination=destinations[destination_name],
                body=body,
                defaults={
                    "rating": Decimal(rating),
                    "review_type": review_type,
                    "is_verified": is_verified,
                },
            )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded: {Traveler.objects.count()} travelers, "
            f"{Destination.objects.count()} destinations, "
            f"{Destination.travelers.through.objects.count()} destination-traveler links, "
            f"{Review.objects.count()} reviews."
        ))
