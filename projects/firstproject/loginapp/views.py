from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import reserve
from datetime import datetime
from django.http import JsonResponse
import json
from django.core import serializers


def index(request):

    return render(request, 'menu.html')

def book(request):

    return render(request, 'loginpage.html')

def Reserve(request):
    data = list(reserve.objects.values())
    context = {
        'data' : data

    }
    return render(request, 'reserve.html' , context)

def bookings_api(request):
    date = request.GET.get('date')
    if date:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            bookings = reserve.objects.filter(date_field=date).values()
            if bookings:
                return JsonResponse({'bookings': list(bookings)})
            else:
                return JsonResponse({'bookings': 'no books are there'})
                                    
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
    else:
        return JsonResponse({'error': 'Date parameter is missing.'}, status=400)
   

# Create your views here.

@csrf_exempt
def test(request):
    ind = False
 
    if request.method == 'POST':

        name = request.POST.get('name')
        time = request.POST.get('time')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")

        message = "This time slot is already existing..."
        existing_reservations = reserve.objects.filter(date_field=date, time_field=time)
        bookdate = f'booked for {date}'
        if existing_reservations:
            ind = True
            # A reservation already exists for the same date and time
            context = {
                'massage': message,
                'obj': reserve.objects.filter(date_field=date),
                'ind': ind,
                'bookdate' : bookdate
            }
            return render(request, 'loginpage.html', context)

        # Create a new reservation
        reservation = reserve(name=name, time_field=time, date_field=date)
        reservation.save()
        message = 'successfully created'
        ind = True
        context = {
            'massage': message,
            'ind': ind,
            'obj': reserve.objects.filter(date_field=date),
            'bookdate' : bookdate
        }
        return render(request, 'loginpage.html', context)

        


        # Handle form submission
        # Retrieve form data using request.POST
    else:
        # Handle GET request
        return render(request, 'test.html')
   
     
     
