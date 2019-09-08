from django.core.exceptions import ValidationError

CATEGORIES = ["Mediterranean", "Indian", "Mexican", "Chinese", "Italian", "Continental"]

def validate_category(value):
    cat = value.capitalize()
    if cat not in CATEGORIES and value not in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
