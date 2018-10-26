from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Root home page")

def random_number(request, max_rand=100):
    random_number = random.randrange(0, int(max_rand))
    msg = "Random nu,ber betwee 0 and %s : %d"%(max_rand, random_number)
    return HttpResponse(msg) 
    # return rand("Root home page")