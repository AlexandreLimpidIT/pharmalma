from django.urls import path
from .views import carte_view

urlpatterns = [
    path('', carte_view, name='carte')
]