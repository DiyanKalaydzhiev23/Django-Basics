from django.db import migrations


DESTINATIONS = [
    {
        "name": "Kyoto",
        "slug": "kyoto-japan",
        "description": "A historic city known for quiet temple gardens, narrow lanes in Gion, seasonal food markets, and maple-lined walks beside the Kamo River.",
        "country": "Japan",
        "is_active": True,
    },
    {
        "name": "Santorini",
        "slug": "santorini-greece",
        "description": "A volcanic island with whitewashed villages, caldera views, black-sand beaches, cliffside paths, and sunset dinners over the Aegean Sea.",
        "country": "Greece",
        "is_active": True,
    },
    {
        "name": "Banff",
        "slug": "banff-canada",
        "description": "A mountain town surrounded by turquoise lakes, alpine trails, glacier viewpoints, wildlife corridors, and cozy lodges in the Canadian Rockies.",
        "country": "Canada",
        "is_active": True,
    },
    {
        "name": "Marrakesh",
        "slug": "marrakesh-morocco",
        "description": "A vivid city of riads, spice stalls, courtyard cafes, palm gardens, tilework, and evening street food around Jemaa el-Fnaa.",
        "country": "Morocco",
        "is_active": True,
    },
    {
        "name": "Reykjavik",
        "slug": "reykjavik-iceland",
        "description": "A compact northern capital with geothermal pools, harbor restaurants, colorful streets, lava-field day trips, and easy access to winter skies.",
        "country": "Iceland",
        "is_active": True,
    },
    {
        "name": "Queenstown",
        "slug": "queenstown-new-zealand",
        "description": "A lakeside adventure base framed by steep peaks, famous for hiking, scenic drives, vineyards, jet boats, and crisp mountain air.",
        "country": "New Zealand",
        "is_active": True,
    },
    {
        "name": "Dubrovnik",
        "slug": "dubrovnik-croatia",
        "description": "A walled Adriatic city with limestone streets, sea kayaking, island ferries, rooftop views, and long golden evenings along the harbor.",
        "country": "Croatia",
        "is_active": True,
    },
    {
        "name": "Petra",
        "slug": "petra-jordan",
        "description": "An ancient rock-cut city reached through a narrow canyon, with desert trails, carved facades, Bedouin tea stops, and starry nights nearby.",
        "country": "Jordan",
        "is_active": True,
    },
    {
        "name": "Cusco",
        "slug": "cusco-peru",
        "description": "A highland city blending Inca stonework, colonial plazas, Andean markets, mountain rail journeys, and gateways to Sacred Valley treks.",
        "country": "Peru",
        "is_active": True,
    },
    {
        "name": "Amalfi Coast",
        "slug": "amalfi-coast-italy",
        "description": "A dramatic coastline of pastel villages, lemon groves, ferry rides, terraced gardens, seafood lunches, and winding roads above the sea.",
        "country": "Italy",
        "is_active": True,
    },
    {
        "name": "Cape Town",
        "slug": "cape-town-south-africa",
        "description": "A coastal city anchored by Table Mountain, with vineyard trips, beaches, design markets, penguin colonies, and a layered cultural history.",
        "country": "South Africa",
        "is_active": True,
    },
    {
        "name": "Hoi An",
        "slug": "hoi-an-vietnam",
        "description": "A lantern-lit riverside town with tailor shops, cooking classes, old merchant houses, cycling routes, and gentle beaches close by.",
        "country": "Vietnam",
        "is_active": True,
    },
    {
        "name": "Edinburgh",
        "slug": "edinburgh-scotland",
        "description": "A walkable capital of stone closes, literary pubs, castle views, festival stages, hilltop paths, and moody streets rich with history.",
        "country": "Scotland",
        "is_active": True,
    },
    {
        "name": "Seville",
        "slug": "seville-spain",
        "description": "A warm Andalusian city of orange trees, shaded plazas, tapas bars, flamenco rooms, tiled palaces, and slow evenings by the river.",
        "country": "Spain",
        "is_active": True,
    },
    {
        "name": "Zermatt",
        "slug": "zermatt-switzerland",
        "description": "A car-free alpine village with Matterhorn views, ski lifts, glacier trails, wooden chalets, and precise mountain hospitality.",
        "country": "Switzerland",
        "is_active": True,
    },
    {
        "name": "Nusa Penida",
        "slug": "nusa-penida-indonesia",
        "description": "A rugged island near Bali with cliff viewpoints, bright coves, manta snorkeling, quiet roads, and simple guesthouses above the coast.",
        "country": "Indonesia",
        "is_active": True,
    },
    {
        "name": "Lisbon",
        "slug": "lisbon-portugal",
        "description": "A hilly Atlantic capital with tiled facades, tram rides, lookout terraces, seafood taverns, live fado, and breezy neighborhoods.",
        "country": "Portugal",
        "is_active": True,
    },
    {
        "name": "Tallinn",
        "slug": "tallinn-estonia",
        "description": "A Baltic city with medieval walls, modern design cafes, harbor walks, craft studios, digital culture, and snowy old-town lanes in winter.",
        "country": "Estonia",
        "is_active": True,
    },
    {
        "name": "Vancouver Island",
        "slug": "vancouver-island-canada",
        "description": "A Pacific island destination with rainforest trails, harbor towns, whale watching, surf beaches, farmers markets, and cedar-lined roads.",
        "country": "Canada",
        "is_active": True,
    },
    {
        "name": "Sapa",
        "slug": "sapa-vietnam",
        "description": "A misty mountain town with rice terraces, village hikes, local homestays, cool evenings, and sweeping views across northern Vietnam.",
        "country": "Vietnam",
        "is_active": True,
    },
]


def seed_destinations(apps, schema_editor):
    Destination = apps.get_model("destinations", "Destination")

    for destination in DESTINATIONS:
        Destination.objects.update_or_create(
            slug=destination["slug"],
            defaults=destination,
        )


def remove_seeded_destinations(apps, schema_editor):
    Destination = apps.get_model("destinations", "Destination")
    Destination.objects.filter(
        slug__in=[destination["slug"] for destination in DESTINATIONS],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("destinations", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_destinations, remove_seeded_destinations),
    ]
