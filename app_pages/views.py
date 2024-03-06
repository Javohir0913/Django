from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def create_page(request, page_number, prev_page=None, next_page=None):
    return render(request, 'page.html', {'page_number': page_number, 'prev_page': prev_page, 'next_page': next_page})
