from django.db import models

class LanguageChoices(models.TextChoices):
    PYTHON = "py", "Python"
    JAVASCRIPT = "js", "JavaScript"
    C = "c", "C"
    C_PLUS_PLUS = "cpp", "C++"
    OTHER = "other", "Other"
