from django.urls import path
from .views import get_certificate

urlpatterns = [
    path('verify/', get_certificate, name='get_certificate'),
]
