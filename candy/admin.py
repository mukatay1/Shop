from django.contrib import admin
from .models import Candy


# Register your models here.
@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'price',
        'image',
        'slug'
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
