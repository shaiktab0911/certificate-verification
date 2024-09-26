from django.contrib import admin
from django.urls import path
from certificates.views import get_certificate, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('verify/', get_certificate, name='get_certificate'),
]
