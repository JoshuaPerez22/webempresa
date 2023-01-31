from django.urls import path
from . import views as services_views

app_name = 'services'

urlpatterns = [
    path('', services_views.services, name='services'),
]