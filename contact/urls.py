from django.urls import path
from . import views as core_views

app_name = 'contact'

urlpatterns = [
    path('', core_views.contact, name='contact'),
]
