# pages/urls.py
from django.urls import path

from .views import HomePageView,AboutPageView #new About


urlpatterns = [
    path('about/', AboutPageView.as_view(),name='about'),#vai apontar para a função aboutpageview
    path('', HomePageView.as_view(), name='home'),#quando for vazio vem pra cá
    
]