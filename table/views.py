from django.shortcuts import render
from django.http import HttpResponse


def show_table(request):
    output = ""
    for i in range(1, 13):
        result = i * 6
        output += "6 x " + str(i) + " = " + str(result) + "<br>"
    return HttpResponse(output)
