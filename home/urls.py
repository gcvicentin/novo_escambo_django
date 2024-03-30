from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('anuncie/', views.anuncie, name = 'anuncie'),
]