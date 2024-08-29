from django.contrib import admin
from apps.base import models

# Register your models here.

@admin.register(models.NewArrivals)
class NewArrivalsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    filter_display = ('title', 'description', 'image')