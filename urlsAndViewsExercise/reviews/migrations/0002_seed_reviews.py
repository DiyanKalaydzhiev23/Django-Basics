from decimal import Decimal

from django.db import migrations


REVIEWS = [
    {
        "destination_slug": "kyoto-japan",
        "author": "Maya Stoyanova",
        "body": "Kyoto felt calm even in the busy areas. The early walk through Fushimi Inari was the highlight, and the small family-run noodle shops made each day easy to enjoy.",
        "rating": "4.90",
        "is_published": True,
    },
    {
        "destination_slug": "santorini-greece",
        "author": "Daniel Petroff",
        "body": "The views from Oia were just as impressive as expected, but the best part was taking a quiet morning ferry and finding a beach taverna before the crowds arrived.",
        "rating": "4.70",
        "is_published": True,
    },
    {
        "destination_slug": "banff-canada",
        "author": "Elena Marinova",
        "body": "Banff was beautifully organized for hikers. Lake Louise was busy, but the trails beyond the main viewpoint opened into peaceful alpine scenery within minutes.",
        "rating": "4.85",
        "is_published": True,
    },
    {
        "destination_slug": "marrakesh-morocco",
        "author": "Nikolay Ivanov",
        "body": "The medina was intense in the best way. Staying in a riad made the trip feel personal, and the rooftop breakfasts were a perfect pause between market walks.",
        "rating": "4.55",
        "is_published": True,
    },
    {
        "destination_slug": "reykjavik-iceland",
        "author": "Sara Dimitrova",
        "body": "Reykjavik was relaxed, friendly, and easy to navigate. The geothermal pools were worth building a whole afternoon around after a windy coastal drive.",
        "rating": "4.60",
        "is_published": True,
    },
    {
        "destination_slug": "queenstown-new-zealand",
        "author": "Adrian Kolev",
        "body": "Queenstown delivered on scenery every single hour. We mixed a lake cruise, a vineyard afternoon, and a long ridge hike without ever needing to rush.",
        "rating": "4.95",
        "is_published": True,
    },
    {
        "destination_slug": "dubrovnik-croatia",
        "author": "Teodora Ilieva",
        "body": "Walking the city walls near closing time was unforgettable. The old town can get crowded, but the side streets still had plenty of quiet corners.",
        "rating": "4.50",
        "is_published": True,
    },
    {
        "destination_slug": "petra-jordan",
        "author": "Martin Georgiev",
        "body": "Petra was far larger than I imagined. Starting early helped with the heat, and the trail to the Monastery was absolutely worth the climb.",
        "rating": "4.80",
        "is_published": True,
    },
    {
        "destination_slug": "cusco-peru",
        "author": "Viktoria Hristova",
        "body": "Cusco had a great balance of history, food, and mountain access. Taking the first day slowly helped with the altitude and made the rest of the trip smoother.",
        "rating": "4.65",
        "is_published": True,
    },
    {
        "destination_slug": "amalfi-coast-italy",
        "author": "Alexandar Todorov",
        "body": "The Amalfi Coast was stunning from the water. Ferries made the villages easier to enjoy, and the lemon desserts in Amalfi were a daily event.",
        "rating": "4.75",
        "is_published": True,
    },
    {
        "destination_slug": "cape-town-south-africa",
        "author": "Irina Nikolova",
        "body": "Cape Town had more variety than any city break I have taken. Table Mountain, the vineyards, and the coastal road each felt like a different trip.",
        "rating": "4.88",
        "is_published": True,
    },
    {
        "destination_slug": "hoi-an-vietnam",
        "author": "Petar Rusev",
        "body": "Hoi An was gentle and memorable. The lanterns are beautiful at night, but cycling to the beach before breakfast was the moment that stayed with me.",
        "rating": "4.68",
        "is_published": True,
    },
    {
        "destination_slug": "edinburgh-scotland",
        "author": "Lora Mihaylova",
        "body": "Edinburgh is perfect for wandering. Every close seemed to lead somewhere interesting, and the view from Arthur's Seat made the rainy walk worthwhile.",
        "rating": "4.62",
        "is_published": True,
    },
    {
        "destination_slug": "seville-spain",
        "author": "Borislav Angelov",
        "body": "Seville was warm, colorful, and easy to love. The tapas scene was excellent, and evenings around Triana felt lively without being overwhelming.",
        "rating": "4.72",
        "is_published": True,
    },
    {
        "destination_slug": "zermatt-switzerland",
        "author": "Gergana Pavlova",
        "body": "Zermatt was clean, quiet, and beautifully run. Even non-skiers in our group had plenty to do with mountain trains, short walks, and long lunches.",
        "rating": "4.58",
        "is_published": True,
    },
    {
        "destination_slug": "nusa-penida-indonesia",
        "author": "Stanislav Vasilev",
        "body": "Nusa Penida felt adventurous without being complicated. The roads take patience, but the viewpoints and snorkeling made the extra effort feel completely fair.",
        "rating": "4.40",
        "is_published": True,
    },
    {
        "destination_slug": "lisbon-portugal",
        "author": "Mila Karadzhova",
        "body": "Lisbon was relaxed, bright, and full of excellent small restaurants. We used the trams sparingly and enjoyed walking between viewpoints at sunset.",
        "rating": "4.78",
        "is_published": True,
    },
    {
        "destination_slug": "tallinn-estonia",
        "author": "Kalin Popov",
        "body": "Tallinn surprised me with how well the old town and modern design areas fit together. It was compact, affordable, and great for a long weekend.",
        "rating": "4.45",
        "is_published": True,
    },
    {
        "destination_slug": "vancouver-island-canada",
        "author": "Yoana Stefanova",
        "body": "Vancouver Island was ideal for a slower trip. The rainforest walks, seafood spots, and harbor mornings made the whole week feel restorative.",
        "rating": "4.82",
        "is_published": True,
    },
    {
        "destination_slug": "sapa-vietnam",
        "author": "Hristo Markov",
        "body": "Sapa was misty, quiet, and incredibly scenic. The guided terrace hike gave useful context, and the homestay dinner was one of the best meals of the trip.",
        "rating": "4.66",
        "is_published": True,
    },
]


def seed_reviews(apps, schema_editor):
    Destination = apps.get_model("destinations", "Destination")
    Review = apps.get_model("reviews", "Review")

    destinations_by_slug = {
        destination.slug: destination
        for destination in Destination.objects.filter(
            slug__in=[review["destination_slug"] for review in REVIEWS],
        )
    }

    for review in REVIEWS:
        destination = destinations_by_slug[review["destination_slug"]]
        Review.objects.update_or_create(
            destination=destination,
            author=review["author"],
            defaults={
                "body": review["body"],
                "rating": Decimal(review["rating"]),
                "is_published": review["is_published"],
            },
        )


def remove_seeded_reviews(apps, schema_editor):
    Destination = apps.get_model("destinations", "Destination")
    Review = apps.get_model("reviews", "Review")

    destinations_by_slug = {
        destination.slug: destination
        for destination in Destination.objects.filter(
            slug__in=[review["destination_slug"] for review in REVIEWS],
        )
    }

    for review in REVIEWS:
        destination = destinations_by_slug.get(review["destination_slug"])

        if destination:
            Review.objects.filter(
                destination=destination,
                author=review["author"],
                body=review["body"],
            ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("destinations", "0002_seed_destinations"),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_reviews, remove_seeded_reviews),
    ]
