from django.core.exceptions import ValidationError

SIZE = 5 * 1024 * 1024


def validate_photo_size_less_than_5mb(value):
    if value.size > SIZE:
        raise ValidationError("File size should less than 5MB")
