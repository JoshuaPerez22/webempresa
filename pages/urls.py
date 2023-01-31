from django.urls import path
from . import views as page_views

app_name = 'page'

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', page_views.page, name='page'),
]