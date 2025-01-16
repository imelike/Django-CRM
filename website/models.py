from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Record(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        unique=True
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def clean(self):
        if not str(self.zipcode).isdigit():  # Burada self.zipcode'un string olduğunu garantiliyoruz
            raise ValidationError({'zipcode': "Zipcode must contain only digits."})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


