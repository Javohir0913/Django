# myapp/urls.py
from django.urls import path
from .views import sahifa_1, sahifa_5, sahifa_4, sahifa_3, sahifa_2, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('page/1', sahifa_1, name='sahifa_1'),
    path('page/2', sahifa_2, name='sahifa_2'),
    path('page/3', sahifa_3, name='sahifa_3'),
    path('page/4', sahifa_4, name='sahifa_4'),
    path('page/5', sahifa_5, name='sahifa_5'),
]