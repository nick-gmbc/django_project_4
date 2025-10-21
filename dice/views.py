from django.shortcuts import render
from django.http import HttpResponse
import random

def throw_dice(request):
    die = random.randint(1,6)
    output = "<h1>You rolled" + str(die) + "</h1>"
    return HttpResponse(output)
