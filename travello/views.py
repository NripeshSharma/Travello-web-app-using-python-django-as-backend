from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    
    # This is all static data
    # dest1 = Destination()
    # dest1.name = 'Varanasi'
    # dest1.desc = 'The city where ganga flows'
    # dest1.price = 800
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True
    
    # dest2 = Destination()
    # dest2.desc = 'Liker State'
    # dest2.name = 'Goa'
    # dest2.price = 1000
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = False
    
    # dest3 = Destination()
    # dest3.name = 'Bangalore'
    # dest3.desc = 'IT Hub'
    # dest3.price = 1500
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False
    
    # dests = [dest1, dest2, dest3]
    
    #To pass data from the database we will use the following
    dests = Destination.objects.all()
    
    return render(request, "index.html", {'dests': dests}) # we are passing an object to index.html
