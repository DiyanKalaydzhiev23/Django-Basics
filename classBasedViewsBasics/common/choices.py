from django.db import models

class CountryChoice(models.TextChoices):
    BULGARIA = "BG", "Bulgaria"
    UNITED_KINGDOM = "UK", "United Kingdom"
    GERMANY = "DE", "Germany"
    FRANCE = "FR", "France"
    ITALY = "IT", "Italy"
    SPAIN = "ES", "Spain"
    USA = "US", "United States"
    CANADA = "CA", "Canada"
    AUSTRALIA = "AU", "Australia"
    OTHER = "OTHER", "Other"
