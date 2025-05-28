from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'days', 'trip_date', 'hotel_class', 'price')
    list_filter = ('country', 'hotel_class', 'trip_date')
    search_fields = ('country', 'city')
    date_hierarchy = 'trip_date'
    ordering = ('-trip_date',)

admin.site.register(Trip, TripAdmin)