from django.http import HttpResponse
from django.shortcuts import render


def hello(request):

    context = {}

    context['hello'] = 'view.py中的传参数｛｛｝｝'
    context['name'] = '徐国忠'
    context['eng'] = 'English'
    context['age'] = 18
    context['data'] = [
        'd1',
        'd2',
        'd3',
     ]

    context['json'] = [
        {"name": "frank", "age": 18},
        {"name": "candy", "age": 15},
        {"name": "dog", "age": 2},
    ]

    return render(request, 'hello.html', context)
