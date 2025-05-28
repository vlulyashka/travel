from django.shortcuts import render
from .models import Trip

def trip_list(request):
    trips = Trip.objects.all().order_by('-trip_date')
    context = {'trips': trips}
    return render(request, 'trips/trip_list.html', context)