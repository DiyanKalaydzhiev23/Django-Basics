from django.db import migrations


CATEGORIES = {
    "Personal": "Everyday personal notes, reminders, and ideas.",
    "Learning": "Study notes, practice topics, and mentoring questions.",
    "Health": "Medical appointments, fitness, and wellness notes.",
    "Projects": "Portfolio, development, and improvement tasks.",
    "Errands": "Short practical tasks and day-to-day chores.",
    "Finance": "Budgeting and money-related notes.",
    "Home": "Apartment upkeep and household cleanup.",
    "Travel": "Trip planning and travel-related notes.",
    "Writing": "Drafts, outlines, and writing ideas.",
    "General": "Unsorted notes that do not fit another category.",
}

NOTE_CATEGORIES = {
    "Grocery list for Sunday dinner": "Personal",
    "Django model reminders": "Learning",
    "Call the dentist": "Health",
    "Books to look for": "Personal",
    "Ideas for portfolio project": "Projects",
    "Weekend errands": "Errands",
    "Meeting notes from study group": "Learning",
    "Birthday gift ideas": "Personal",
    "Fix laptop setup": "Projects",
    "Recipe experiment": "Personal",
    "Questions for mentor": "Learning",
    "Monthly budget check": "Finance",
    "Tiny UI improvements": "Projects",
    "Trip planning notes": "Travel",
    "Practice SQL joins": "Learning",
    "Apartment maintenance": "Home",
    "Article draft outline": "Writing",
    "Workout plan": "Health",
    "Code review checklist": "Projects",
    "Things to clean up later": "Home",
}


def populate_categories(apps, schema_editor):
    Category = apps.get_model("categories", "Category")
    Note = apps.get_model("notes", "Note")

    categories = {}
    for name, description in CATEGORIES.items():
        category, _ = Category.objects.update_or_create(
            name=name,
            defaults={"description": description},
        )
        categories[name] = category

    for title, category_name in NOTE_CATEGORIES.items():
        Note.objects.filter(title=title).update(category=categories[category_name])

    Note.objects.filter(category__isnull=True).update(category=categories["General"])


def unpopulate_categories(apps, schema_editor):
    Category = apps.get_model("categories", "Category")
    Note = apps.get_model("notes", "Note")

    category_names = list(CATEGORIES)
    Note.objects.filter(category__name__in=category_names).update(category=None)
    Category.objects.filter(name__in=category_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("notes", "0002_note_category"),
    ]

    operations = [
        migrations.RunPython(populate_categories, unpopulate_categories),
    ]
