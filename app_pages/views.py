from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def sahifa_1(request):
    return HttpResponse('<h1>1 - sahifa</h1><br>'
                        '<a href=2>keyingi sahifa</a>')


def sahifa_2(request):
    return HttpResponse('<h1>2 - sahifa</h1><br>'
                        '<a href=1>oldingi sahifa</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                        '<a href=3>keyingi sahifa</a>')


def sahifa_3(request):
    return HttpResponse('<h1>3 - sahifa</h1><br>'
                        '<a href=2>oldingi sahifa</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                        '<a href=4>keyingi sahifa</a>')


def sahifa_4(request):
    return HttpResponse('<h1>4 - sahifa</h1><br>'
                        '<a href=3>oldingi sahifa</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                        '<a href=5>keyingi sahifa</a>')


def sahifa_5(request):
    return HttpResponse('<h1>5 - sahifa</h1><br>'
                        '<a href=4>oldingi sahifa</a>')
