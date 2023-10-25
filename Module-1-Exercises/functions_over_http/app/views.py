from django.http.response import HttpResponse
from django.http.request import HttpRequest

import random


def hello_view(request: HttpRequest, name):
    return HttpResponse(f'Hello {name}')


def roll_die_view(request: HttpRequest, sides):
    roll = random.randint(1, sides)
    return HttpResponse(roll)


def random_between_view(request, lo, hi):
    return HttpResponse(random.randint(lo, hi))

def add_view(request, num1, num2):
    return HttpResponse(num1 + num2)

def hey_view(request, name):
    return HttpResponse(f'Hey, {name}!')

def age_in_view(request, Year, BirthYear):
    return HttpResponse(Year - BirthYear)

def order_total_view(request, burg, fry, drinks):
    return HttpResponse((burg*4.5)+(fry*1.5)+drinks)

