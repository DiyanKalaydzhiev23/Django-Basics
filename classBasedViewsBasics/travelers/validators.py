from django.core.exceptions import ValidationError


def validate_email_domain(value):
    allowed_domains = ["university.com", "university.org"]
    if not any(value.endswith(domain) for domain in allowed_domains):
        raise ValidationError(f"Email domain must be one of {', '.join(allowed_domains)}")
