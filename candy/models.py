from django.core.validators import MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Candy(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    price = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator,
        ]
    )
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = 'Сладости'
        verbose_name_plural = 'Сладости'

    def __str__(self):
        return self.name
