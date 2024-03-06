from django.urls import path
from .views import HomePageView, create_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('page/1', create_page, {'page_number': 1, 'next_page': 2}, name='page_1'),
    path('page/2', create_page, {'page_number': 2, 'prev_page': 1, 'next_page': 3}, name='page_2'),
    path('page/3', create_page, {'page_number': 3, 'prev_page': 2, 'next_page': 4}, name='page_3'),
    path('page/4', create_page, {'page_number': 4, 'prev_page': 3, 'next_page': 5}, name="page_4"),
    path('page/5', create_page, {'page_number': 5, 'prev_page': 4}, name='page_5'),
]